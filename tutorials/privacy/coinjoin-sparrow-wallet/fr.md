---
name: Coinjoin - Sparrow Wallet
description: Comment faire un coinjoin sur Sparrow Wallet ?
---
![cover](assets/cover.webp)

Dans ce tutoriel, vous allez apprendre ce qu'est un coinjoin et comment en réaliser avec le logiciel Sparrow Wallet et l'implémentation Whirlpool.

## Qu'est-ce qu'un coinjoin sur Bitcoin ?
**Le coinjoin est une technique qui permet de casser le traçage des bitcoins sur la blockchain**. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction coinjoin.

Les transactions coinjoin renforcent la confidentialité des utilisateurs de Bitcoin en complexifiant l'analyse de chaîne pour les observateurs externes. Leur structure permet de fusionner plusieurs pièces de différents utilisateurs en une unique transaction, brouillant ainsi les pistes et rendant difficile la détermination des liens entre les adresses d'entrée et de sortie.

Le principe du coinjoin repose sur une approche collaborative : plusieurs utilisateurs qui souhaitent mélanger leurs bitcoins déposent des montants identiques en entrées d'une même transaction. Ces montants sont ensuite redistribués en sorties de valeur égale. À l'issue de la transaction, il devient impossible d'associer un output spécifique à un utilisateur donné. Aucun lien direct n'existe entre les entrées et les sorties, ce qui vient rompre l'association entre les utilisateurs et leurs UTXO, de même que l'historique de chaque pièce.
![coinjoin](assets/fr/1.webp)

Exemple d'une transaction coinjoin : [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/fr/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Afin de réaliser un coinjoin tout en garantissant que chaque utilisateur conserve le contrôle sur ses fonds à tout moment, le processus débute par la construction de la transaction par un coordinateur, qui la transmet ensuite à chaque participant. Chaque utilisateur procède alors à la signature de la transaction après avoir vérifié que celle-ci lui convient. Toutes les signatures collectées sont finalement intégrées à la transaction. Si une tentative de détournement des fonds est effectuée par un utilisateur ou le coordinateur, par le biais d'une modification des outputs de la transaction coinjoin, les signatures se révéleront invalides, ce qui conduira au rejet de la transaction par les nœuds.

Il existe plusieurs implémentations de coinjoin, telles que Whirlpool, JoinMarket ou Wabisabi, chacune ayant pour objectif de gérer la coordination entre les participants et d'accroître l'efficacité des transactions coinjoin.

Dans ce tutoriel, nous nous penchons sur l'implémentation **Whirlpool**, que je considère comme la solution la plus efficace pour faire des coinjoins sur Bitcoin. Bien que disponible sur plusieurs portefeuilles, nous explorons dans ce tutoriel exclusivement l'utilisation avec le logiciel Desktop Sparrow Wallet.

## Pourquoi faire des coinjoins sur Bitcoin ?
Un des problèmes initiaux à tout système de paiement pair-à-pair est la double dépense : comment empêcher des individus mal intentionnés de dépenser à plusieurs reprises les mêmes unités monétaires sans faire appel à une autorité centrale pour arbitrer ?

Satoshi Nakamoto a apporté une solution à ce dilemme au travers du protocole Bitcoin, un système de paiement électronique pair-à-pair qui fonctionne indépendamment de toute autorité centrale. Dans son livre blanc, il souligne que la seule manière de certifier l'absence de double dépense est d'assurer la visibilité de toutes les transactions au sein du réseau de paiement.

Afin de garantir que chaque participant soit au courant des transactions, ces dernières doivent être publiquement divulguées. Le fonctionnement de Bitcoin repose donc sur une infrastructure transparente et distribuée, permettant à tout opérateur de nœud de vérifier l'intégralité des chaines de signatures électroniques et l'historique de chaque pièce, depuis sa création par un mineur.

La nature transparente et distribuée de la blockchain de Bitcoin signifie que tout utilisateur du réseau peut suivre et analyser les transactions de tous les autres participants. En conséquence, l'anonymat au niveau des transactions est impossible. Cependant, l'anonymat est préservé au niveau de l'identification des individus. Contrairement au système bancaire classique où chaque compte est lié à une identité personnelle, sur Bitcoin, les fonds sont associés à des paires de clés cryptographiques, offrant ainsi aux utilisateurs une forme de pseudonymat derrière des identifiants cryptographiques.

Ainsi, la confidentialité sur Bitcoin est mise à mal lorsque des observateurs extérieurs parviennent à associer des UTXO spécifiques à des utilisateurs identifiés. Une fois cette association établie, il devient possible de tracer leurs transactions et d'analyser l'historique de leurs bitcoins. Le coinjoin est justement une technique développée pour casser la traçabilité des UTXO, offrant ainsi une certaine couche de confidentialité aux utilisateurs de Bitcoin au niveau des transactions.

## Comment fonctionne Whirlpool ?
Whirlpool se distingue des autres méthodes de coinjoin par l'utilisation de transactions "_ZeroLink_", qui assurent qu'il n'y a strictement aucun lien technique possible entre tous les inputs et tous les outputs. Ce mixage parfait est obtenu grâce à une structure où chaque participant contribue avec un montant identique en input (à l'exception des frais de minage), générant ainsi des outputs de montant égaux.

Cette approche restrictive sur les inputs confère aux transactions coinjoin de Whirlpool une caractéristique unique : l'absence totale de liens déterministes entre les inputs et les outputs. Autrement dit, chaque output possède une probabilité égale d'être attribué à n'importe quel participant, par rapport à tous les autres outputs de la transaction.

Initialement, le nombre de participants à chaque coinjoin Whirlpool était limité à 5, avec 2 nouveaux entrants et 3 rémixeurs (nous expliquerons ces concepts plus loin). Toutefois, l'augmentation des frais de transaction on-chain observée en 2023 a incité les équipes de Samourai à repenser leur modèle pour améliorer la confidentialité tout en réduisant les coûts. Ainsi, en tenant compte de la situation du marché des frais et du nombre de participants, le coordinateur peut désormais organiser des coinjoins incluant 6, 7 ou 8 participants. Ces sessions améliorées sont désignées sous le nom de "_Surge Cycles_". Il est important de noter que, quelle que soit la configuration, il y a toujours uniquement 2 nouveaux entrants dans les coinjoins Whirlpool.

Ainsi, les transactions Whirlpool se caractérisent par un nombre identique d'inputs et d'outputs, pouvant être de :
- 5 inputs et 5 outputs ;
![coinjoin](assets/fr/2.webp)
- 6 inputs et 6 outputs ;
![coinjoin](assets/fr/3.webp)
- 7 inputs et 7 outputs ;
![coinjoin](assets/fr/4.webp)
- 8 inputs et 8 outputs.
![coinjoin](assets/fr/5.webp)
Le modèle proposé par Whirlpool est ainsi basé sur de petites transactions coinjoin. À la différence de Wabisabi et JoinMarket, où la robustesse des anonsets repose sur le volume de participants sur un cycle unique, Whirlpool mise sur l'enchainement de plusieurs cycles de petite taille.

Dans ce modèle, l'utilisateur s'acquitte des frais uniquement lors de son entrée initiale dans une pool, lui permettant ensuite de participer à une multitude de remixages sans frais supplémentaires. Ce sont les nouveaux entrants qui prennent en charge les frais de minage pour les remixeurs.

Ainsi, à chaque étape de remixage à laquelle participe l'utilisateur, ainsi que ses pairs rencontrés par le passé, les anonsets vont croitre exponentiellement. L'objectif est donc de profiter de ces remixages gratuits qui, à chaque occurrence, contribuent à renforcer la densité des anonsets associés à chaque pièce mixée.

Whirlpool a été conçu en prenant en compte deux exigences importantes :
- L'accessibilité de l'implémentation sur appareils mobiles, étant donné que Samourai Wallet est avant tout une application de smartphone ;
- La rapidité des cycles de remixage pour favoriser une augmentation significative des anonsets.

Ces impératifs ont guidé les choix des développeurs de Samourai Wallet dans la conception de Whirlpool, les amenant à restreindre le nombre de participants à un nombre limité par cycle. Un nombre trop restreint aurait compromis l'efficacité du coinjoin, réduisant drastiquement les anonsets générés à chaque cycle, tandis qu'un nombre trop important aurait posé des problèmes de gestion sur les applications mobiles et aurait entravé le flux de cycles.

**Finalement, nul besoin d'avoir un nombre élevé de participants par coinjoin sur Whirlpool puisque les anonsets se font sur l'accumulation de plusieurs cycles de mixage.**

[-> En savoir plus sur les anonsets Whirlpool.](https://planb.network/tutorials/privacy/wst-anonsets)

### Les pools et les frais de coinjoin
Pour que ces multiples cycles permettent bien de faire augmenter les anonsets des pièces mixées, il faut mettre un certain cadre afin de restreindre les montants des UTXO utilisés. Whirlpool défini ainsi différentes pools.

Une pool représente un ensemble d'utilisateurs souhaitant mixer ensemble, qui s'accorde sur le montant des UTXO à utiliser pour optimiser le processus de coinjoin. Chaque pool spécifie un montant fixe pour l'UTXO, auquel l'utilisateur doit se conformer pour y participer. Ainsi, pour entreprendre des coinjoins avec Whirlpool, il vous faut sélectionner une pool adéquate où entamer le processus de mixage. Les pools disponibles sur Whirlpool à l'heure actuelle sont les suivantes :
- 0,5 bitcoins ;
- 0,05 bitcoin ;
- 0,01 bitcoin ;
- 0,001 bitcoin (= 100 000 sats).

En intégrant une pool avec vos bitcoins, ceux-ci seront divisés afin de générer des UTXO parfaitement homogènes avec ceux des autres participants de la pool. Chaque pool possède une limite maximale ; ainsi, pour des montants excédant cette limite, vous serez contraint soit d'effectuer deux entrées distinctes au sein de la même pool, soit de vous orienter vers une autre pool de montant supérieur :

| Pool (bitcoin) | Montant maximum par entrée (bitcoin) |
|----------------|--------------------------------------|
| 0,5            | 35                                   |
| 0,05           | 3,5                                  |
| 0,01           | 0,7                                  |
| 0,001          | 0,025                                |

Comme mentionné précédemment, un UTXO est considéré comme appartenant à une pool lorsqu'il est prêt à être intégré dans un coinjoin. Cela ne signifie toutefois pas que l'utilisateur en perd la possession. À travers les différents cycles de mixage, vous conservez intégralement le contrôle de vos clés et, par conséquent, de vos bitcoins.

Pour entrer dans une pool de coinjoin, il faut régler des frais de service ainsi que des frais de minage. Les frais de service sont fixes pour chaque pool et sont destinés à rémunérer les équipes en charge du développement et de la maintenance de Whirlpool. Pour les utilisateurs de Sparrow Wallet, ces frais sont reversés par les équipes de Samourai aux développeurs de Sparrow.

Les frais de service pour l'utilisation de Whirlpool sont à régler une unique fois à l'entrée dans la pool. Une fois cette étape franchie, vous avez la possibilité de participer à un nombre illimité de remixages sans frais supplémentaires. Voici les frais fixes actuellement appliqués pour chaque pool :

| Pool (bitcoin) | Frais d'entrée (bitcoin)        |
|----------------|---------------------------------|
| 0,5            | 0,0175                          |
| 0,05           | 0,00175                         |
| 0,01           | 0,0005 (50 000 sats)            |
| 0,001          | 0,00005 (5 000 sats)            |

Ces frais fonctionnent essentiellement comme un billet d'entrée pour la pool choisie, indépendamment de la somme que vous mettez en coinjoin. Ainsi, que vous intégriez la pool 0,01 avec exactement 0,01 BTC ou que vous y entriez avec 0,5 BTC, les frais demeureront identiques en valeur absolue.

Avant de procéder au coinjoins, l'utilisateur a donc le choix entre 2 stratégies : 
- Opter pour une pool plus petite afin de minimiser les frais de service, sachant qu'il obtiendra en retour plusieurs petits UTXO ;
- Ou bien privilégier une pool de plus grande taille, acceptant de régler des frais plus élevés pour finalement se retrouver avec un nombre réduit d'UTXO de plus grande valeur. 

Il est généralement déconseillé de fusionner plusieurs UTXO mixés après les cycles de coinjoins, car cela pourrait compromettre la confidentialité acquise, en particulier en raison de l'heuristique de possession commune des entrées (CIOH : *Common-Input-Ownership-Heuristic*). Par conséquent, il peut être judicieux de choisir une pool plus importante, même si cela implique de payer davantage, pour éviter d'avoir trop d'UTXO de petites valeurs en sortie. L'utilisateur doit évaluer ces compromis pour choisir la pool qu'il préfère.

Outre les frais de service, les frais de minage propres à toute transaction Bitcoin doivent également être pris en compte. En tant qu'utilisateur de Whirlpool, vous serez tenu de payer les frais de minage de la transaction de préparation (`Tx0`) ainsi que ceux du premier coinjoin. Tous les remixages ultérieurs seront gratuits, grâce au modèle de Whirlpool qui repose sur le paiement des nouveaux entrants.

En effet, dans chaque coinjoin Whirlpool, deux utilisateurs parmi les entrées sont des entrants. Les autres inputs proviennent de remixeurs. De ce fait, les frais de minage pour l'ensemble des participants de la transaction sont pris en charge par ces deux nouveaux participants, qui pourront ensuite bénéficier eux aussi de remixages gratuits :
![coinjoin](assets/fr/6.webp)
Grâce à ce système de frais, Whirlpool se différencie réellement des autres services de coinjoin puisque les anonsets des UTXO ne sont pas proportionnels au prix payé par l'utilisateur. Ainsi, il est possible d'atteindre des niveaux d'anonymat considérablement élevés en ne s'acquittant que des frais d'entrée de la pool et des frais de minage pour deux transactions (la `Tx0` et le mix initial).

Il est important de noter que l'utilisateur devra également prendre en charge les frais de minage pour retirer ses UTXO de la pool après avoir réalisé ses multiples remixages, sauf s'il a sélectionné l'option `mix to`, dont nous parleront dans le tutoriel ci-dessous.

### Les comptes du portefeuille HD utilisés par Whirlpool
Pour réaliser un coinjoin via Whirlpool, le portefeuille doit générer plusieurs comptes distincts. Un compte, dans le contexte d'un portefeuille HD (*Hierarchical Deterministic*), constitue une section entièrement isolée des autres, cette séparation intervenant au niveau de la troisième profondeur de hiérarchie du portefeuille, c'est-à-dire au niveau des `xpub`.

Un portefeuille HD peut théoriquement dériver jusqu'à `2^(32/2)` comptes différents. Le compte initial, utilisé par défaut sur tous les portefeuille Bitcoin, correspond à l'index `0'`.

Pour les portefeuilles adaptés à Whirlpool, tels que Samourai ou Sparrow, 4 comptes sont utilisés pour répondre aux besoins du processus de coinjoin :
- Le compte **dépôt**, identifié par l'index `0'` ;
- Le compte **bad bank** (ou doxxic change), identifié par l'index `2 147 483 644'` ;
- Le compte **premix**, identifié par l'index `2 147 483 645'` ;
- Le compte **postmix**, identifié par l'index `2 147 483 646'`.

Chacun de ces comptes remplit une fonction particulière dans le cadre du coinjoin.

Tous ces comptes sont liés à une unique graine (seed), ce qui permet à l'utilisateur de récupérer l'accès à l'ensemble de ses fonds en utilisant sa phrase de récupération et, le cas échéant, une passphrase. Il est cependant nécessaire de préciser au logiciel, lors de cette opération de récupération, les différents index de comptes qui ont été utilisés.

Voyons maintenant les différentes étapes d'un coinjoin Whirlpool au sein de ces comptes.

### Les différentes étapes des coinjoins sur Whirlpool
**Étape 1 : La Tx0 :**
Le point de départ de tout coinjoin Whirlpool est le compte **dépôt**. Ce compte est celui que vous utilisez automatiquement lorsque vous établissez un nouveau portefeuille Bitcoin. Ce compte devra être crédité des bitcoins que l'on souhaite mixer.

La `Tx0` représente la première étape du processus de mixage de Whirlpool. Elle vise à préparer et à égaliser les UTXO pour le mixage, en les divisant en unités correspondant au montant de la pool sélectionnée, afin d'assurer l'homogénéité du mixage. Les UTXO ainsi égalisés sont ensuite envoyés vers le compte **premix**. Quant à la différence ne pouvant pas entrer dans la pool, elle est séparée sur un compte spécifique : le **bad bank** (ou "doxxic change").

Cette transaction initiale `Tx0` sert aussi à régler les frais de service dus au coordinateur du mix. Contrairement aux étapes suivantes, cette transaction n'est pas collaborative ; l'utilisateur doit donc assumer l'intégralité des frais de minage :
![coinjoin](assets/fr/7.webp)

Dans cet exemple d'une transaction `Tx0`, un input de `372 000 sats` issu de notre compte dépôt est divisé en plusieurs UTXO en sortie, qui se répartissent comme suit :
- Un montant de `5 000 sats` destiné aux frais du coordinateur, correspondant à l'entrée dans la pool de `100 000 sats` ;
- Trois UTXO préparés pour le mixage, redirigés vers notre compte **premix** et enregistrés auprès du coordinateur. Ces UTXO sont égalisés à `108 000 sats` chacun, afin de couvrir les frais de minage pour leur futur mix initial ;
- Le surplus ne répondant pas aux critères de la pool, considéré comme change toxique, est envoyé vers son compte spécifique. Ici, ce change s'élève à `40 000 sats` ;
- Enfin, il reste `3 000 sats` qui ne constituent pas un output, mais qui sont les frais de minage nécessaires pour confirmer la `Tx0`.

Par exemple, voici une vraie Tx0 Whirlpool (qui ne provient pas de moi) : [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/fr/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Étape 2 : Le doxxic change**
Le surplus n'ayant pas pu intégrer la pool, ici équivalent à `40 000 sats`, est redirigé vers le compte **bad bank**, également désigné sous le terme de "doxxic change", pour en assurer une séparation stricte avec les autres UTXO.

Cet UTXO est dangereux pour la confidentialité de l'utilisateur, car non seulement il est toujours attaché à son passé, et donc éventuellement à l'identité de son propriétaire, mais en plus, il est noté comme appartenant à un utilisateur qui a fait un coinjoin.

Si cet UTXO est fusionné avec des UTXO mixés, ces derniers perdront toute la confidentialité gagnée durant les cycles de coinjoins, notamment à cause de la CIOH (*Common-Input-Ownership-Heuristic*). S'il est fusionné avec d'autres doxxic changes, l'utilisateur risque de perdre en confidentialité puisque cela viendra faire un lien entre les différentes entrées des cycles de coinjoins. Il faut donc le traiter avec prudence. La manière de gérer cet UTXO toxique sera détaillée dans la dernière partie de cet article, et des tutoriels futurs aborderont ces méthodes plus en profondeur.

**Étape 3 : Le mix initial**
Après la réalisation de la `Tx0`, les UTXO égalisés sont envoyés sur le compte **premix** de notre portefeuille, prêts à être introduits dans leur premier cycle de coinjoin, également appelé "mix initial". Si, comme dans notre exemple, la `Tx0` génère plusieurs UTXO destinés au mixage, chacun d'entre eux sera intégré dans un mix initial distinct.

Au terme de ces premiers mixes, le compte **premix** sera vide, tandis que nos pièces, ayant acquitté les frais de minage pour ce premier coinjoin, seront ajustées exactement au montant défini par la pool choisie. Dans notre exemple, nos UTXO initiaux de `108 000 sats` auront été réduits à exactement `100 000 sats`.
![coinjoin](assets/fr/8.webp)
**Étape 4 : Les remix**
Après avoir fait le mix initial, les UTXO sont transférés dans le compte **postmix**. Ce compte rassemble les UTXO déjà mixés et ceux en attente de remix. Lorsque le client Whirlpool est actif, les UTXO situés dans le compte **postmix** sont automatiquement disponibles pour des remixages et seront choisis de manière aléatoire pour participer à ces nouveaux cycles.

Pour rappel, les remix sont ensuite à 100% gratuits : aucun frais de service additionnel ou frais de minage n'est requis. Conserver les UTXO dans le compte **postmix** maintient donc leur valeur intacte, et améliore en même temps leurs anonsets. Voilà pourquoi il est important de permettre à ces pièces de participer à plusieurs cycles de coinjoins. Cela ne vous coute strictement rien, et cela permet d'augmenter leurs niveaux d'anonymat.

Lorsque vous décidez de dépenser des UTXO mixés, vous pouvez le faire directement depuis ce compte **postmix**. Il est conseillé de garder les UTXO mixés dans ce compte pour bénéficier de remixages gratuits et pour éviter qu'ils ne quittent le circuit de Whirlpool, ce qui pourrait diminuer leur confidentialité.

Comme nous le verrons dans le tutoriel suivant, il y a également l'option `mix to` qui offre la possibilité d'envoyer automatiquement vos pièces mixées vers un autre portefeuille, tel qu'un cold wallet, après un nombre défini de coinjoins.

Après avoir abordé la théorie, plongeons dans la pratique avec un tutoriel sur l'utilisation de Whirlpool via le logiciel desktop Sparrow Wallet !

## Tutoriel : Whirlpool sur Sparrow Wallet







### Comment connaître la qualité de nos cycles de coinjoin ?
Pour qu'un coinjoin soit véritablement efficace, il est essentiel qu'il présente une bonne homogénéité entre les montants des inputs et des outputs. Cette uniformité amplifie le nombre d'interprétations possibles aux yeux d'un observateur externe, augmentant ainsi l'incertitude autour de la transaction. Pour quantifier cette incertitude générée par un coinjoin, on peut recourir au calcul de l'entropie de la transaction. Pour une exploration approfondie de ces indicateurs, je vous renvoie vers le tutoriel : [BOLTZMANN CALCULATOR](https://planb.network/fr/tutorials/privacy/boltzmann-entropy). Le modèle de Whirlpool est reconnu comme celui qui apporte le plus d'homogénéité dans les coinjoins.

Ensuite, la performance de plusieurs cycles de coinjoin est évaluée selon l'ampleur des groupes dans lesquels une pièce est dissimulée. La dimension de ces groupes définit ce qu'on nomme les anonsets. Il existe deux types d'anonsets : le premier évalue la confidentialité obtenue contre une analyse rétrospective (du présent vers le passé) et le second, contre une analyse prospective (du passé vers le présent). Pour une explication détaillée de ces deux indicateurs, je vous invite à consulter le tutoriel : [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/wst-anonsets).

### Comment gérer le postmix ?
Après avoir effectué des cycles de coinjoins, la meilleure stratégie consiste à garder vos UTXO dans le compte **postmix**, en attente de leur utilisation future. Il est même conseillé de les laisser se remixer indéfiniment jusqu'à ce que vous ayez besoin de les dépenser.

Certains utilisateurs pourraient envisager de transférer leurs bitcoins mixés vers un portefeuille sécurisé par un hardware wallet. Cela est possible, mais il est important de suivre scrupuleusement les recommandations de Samourai Wallet pour ne pas compromettre la confidentialité acquise.

La fusion d'UTXO constitue l'erreur la plus fréquemment commise. Il faut éviter de combiner dans une même transaction des UTXO mixés avec des UTXO non mixés, afin d'éviter la CIOH (*Common-Input-Ownership-Heuristic*). Cela nécessite une gestion minutieuse de vos UTXO au sein de votre portefeuille, notamment au niveau de l'étiquetage. Au-delà du coinjoin, la fusion d'UTXO est une mauvaise pratique en général qui mène souvent à une perte de confidentialité lorsqu'elle n'est pas maîtrisée.

Il faut également être vigilant sur la consolidation d'UTXO mixés entre eux. Des consolidations modérées sont envisageables si vos UTXO mixés disposent d'anonsets significatifs, mais cela viendra forcément diminuer la confidentialité de vos pièces. Veillez à ce que les consolidations ne soient ni trop importantes, ni réalisées après un nombre insuffisant de remixages, au risque d'établir des liens déductibles entre vos UTXO avant et après les cycles de coinjoins. En cas de doute sur ces manipulations, la meilleure pratique est de ne pas consolider les UTXO postmix, et de les transférer un à un vers votre hardware wallet, en générant à chaque fois une nouvelle adresse vierge. Encore une fois, pensez à bien étiqueter chaque UTXO reçu.

Il est également déconseillé de transférer vos UTXO postmix vers un portefeuille utilisant des scripts peu répandus. Par exemple, si vous entrez sur Whirlpool depuis un portefeuille multisig utilisant des scripts `P2WSH`, il y a peu de chance que vous soyez mélangés avec d'autres utilisateurs ayant le même type de portefeuille à l'origine. Si vous ressortez vos postmix vers ce même portefeuille multisig, le niveau de confidentialité de vos bitcoins mixés sera fortement diminué. Au-delà des scripts, il existe de nombreuses autres empreintes de portefeuille qui peuvent vous jouer des tours.

Comme pour toute transaction Bitcoin, il convient également de ne pas réutiliser les adresses de réception. Chaque nouvelle transaction doit être reçue sur une nouvelle adresse vierge.

La solution la plus simple et la plus sûre consiste à laisser vos UTXO mixés au repos dans leur compte **postmix**, en les laissant se remixer et en ne les touchant que pour les dépenser. Les portefeuilles Samourai et Sparrow disposent de protections supplémentaires contre tous ces risques liés à l'analyse de chaîne. Ces protections vous permettent d'éviter de faire des erreurs.

### Comment gérer le doxxic change ?
Ensuite, il faudra être prudent sur sa gestion du doxxic change, le change qui n'a pas pu entrer dans la pool de coinjoin. Ces UTXO toxiques, issus de l'utilisation de Whirlpool, constituent un risque pour votre vie privée puisqu'ils établissent un lien entre vous et l'utilisation du coinjoin. Il est donc impératif de les gérer avec prudence et de ne pas les combiner avec d'autres UTXO, surtout des UTXO mixés. Voici différentes stratégies à envisager pour les utiliser :
- **Mixez-les dans des pools plus petites :** Si votre UTXO toxique est suffisamment important pour entrer seul dans une pool de taille inférieure, envisagez de le mixer. C'est souvent la meilleure option. Cependant, il est crucial de ne pas fusionner plusieurs UTXO toxiques pour accéder à une pool, car cela pourrait relier vos différentes entrées ;
- **Marquez-les comme "non dépensables" :** Une autre approche consiste à ne plus les utiliser et à les marquer comme "non dépensables" dans leur compte dédié, vous assurant ainsi de ne pas les dépenser accidentellement. Si la valeur du bitcoin augmente, de nouvelles pools plus adaptées à vos UTXO toxiques pourraient voir le jour ;
- **Faites des donations :** Pensez à faire des dons, même modestes, aux développeurs œuvrant sur Bitcoin et ses logiciels associés. Vous pouvez aussi donner à des associations acceptant le BTC. Si la gestion de vos UTXO toxiques vous semble trop compliquée, vous pouvez simplement vous en débarrasser en profitant pour en faire une donation ;
- **Achetez des cartes cadeaux :** Des plateformes telles que [Bitrefill](https://www.bitrefill.com/) vous permettent d'échanger des bitcoins contre des cartes cadeaux utilisables chez divers commerçants. Cela peut être une manière de vous séparer de vos UTXO toxiques sans perdre la valeur associée ;
- **Consolidez-les sur Monero :** Samourai Wallet offre désormais un service de swap atomique entre BTC et XMR. C'est idéal pour gérer les UTXO toxiques en les consolidant sur Monero, sans compromettre votre confidentialité via la CIOH, avant de les renvoyer sur Bitcoin. Cette option peut toutefois s'avérer coûteuse en termes de frais de minage et de premium du aux contraintes de liquidité ;
- **Envoyez-les sur le Lightning Network :** Transférer ces UTXO sur le Lightning Network pour bénéficier de frais de transaction réduits est une option qui peut être intéressante. Cependant, cette méthode peut révéler certaines informations selon votre utilisation du Lightning Network et doit donc être pratiquée avec prudence.

Des tutoriels détaillés sur la mise en œuvre de ces différentes techniques vous seront proposés prochainement sur PlanB Network.

**Ressources supplémentaires :** 
- [Tutoriel vidéo Sparrow Wallet](https://planb.network/tutorials/wallet/sparrow) ;
- [Tutoriel vidéo Samourai Wallet](https://planb.network/tutorials/wallet/samourai) ;
- [Documentation Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts) ;
- [Thread Twitter sur les coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739) ;
- [Article de blog sur les coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin) ;
- [Tutoriel Bitcoin Magazine sur Whirlpool.](https://bitcoinmagazine.com/technical/how-to-whirlpool-bitcoin-sparrow-wallet)
