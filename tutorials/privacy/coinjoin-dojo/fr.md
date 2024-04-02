---
name: Coinjoin - Dojo
description: Comment faire un coinjoin avec son propre Dojo ?
---
![cover](assets/cover.jpeg)

Dans ce tutoriel, vous allez apprendre ce qu'est un coinjoin et comment en réaliser avec le logiciel Samourai Wallet et l'implémentation Whirlpool, en utilisant votre propre Dojo. Cette méthode est selon moi la meilleure à l'heure actuelle pour mixer ses bitcoins.

## Qu'est-ce qu'un coinjoin sur Bitcoin ?
**Le coinjoin est une technique qui permet de casser le traçage des bitcoins sur la blockchain**. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction coinjoin.

Les coinjoins renforcent la confidentialité des utilisateurs de Bitcoin en complexifiant l'analyse de chaîne pour les observateurs externes. Leur structure permet de fusionner plusieurs pièces de différents utilisateurs en une unique transaction, brouillant ainsi les pistes et rendant difficile la détermination des liens entre les adresses d'entrée et de sortie.

Le principe du coinjoin repose sur une approche collaborative : plusieurs utilisateurs qui souhaitent mélanger leurs bitcoins déposent des montants identiques en inputs d'une même transaction. Ces montants sont ensuite redistribués en outputs de valeur égale à chaque utilisateur. À l'issue de la transaction, il devient impossible d'associer un output spécifique à un utilisateur connu en entrée. Aucun lien direct n'existe entre les entrées et les sorties, ce qui vient rompre l'association entre les utilisateurs et leurs UTXO, de même que l'historique de chaque pièce.
![coinjoin](assets/fr/1.webp)

Exemple d'une transaction coinjoin (qui ne provient pas de moi) : [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/fr/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Afin de réaliser un coinjoin tout en garantissant que chaque utilisateur conserve le contrôle sur ses fonds à tout moment, le processus débute par la construction de la transaction par un coordinateur, qui la transmet ensuite aux participants. Chaque utilisateur procède alors à la signature de la transaction après avoir vérifié que celle-ci lui convient. Toutes les signatures collectées sont finalement intégrées à la transaction. Si une tentative de détournement des fonds est effectuée par un utilisateur ou le coordinateur, par le biais d'une modification des outputs de la transaction coinjoin, les signatures se révéleront invalides, ce qui conduira au rejet de la transaction par les nœuds.

Il existe plusieurs implémentations de coinjoin, telles que Whirlpool, JoinMarket ou Wabisabi, chacune ayant pour objectif de gérer la coordination entre les participants et d'accroître l'efficacité des transactions coinjoin.

Dans ce tutoriel, nous nous penchons sur l'implémentation **Whirlpool**, que je considère comme la solution la plus efficace pour faire des coinjoins sur Bitcoin. Bien que disponible sur plusieurs portefeuilles, nous explorons dans ce tutoriel exclusivement l'utilisation avec l'application mobile Samourai Wallet, sans Dojo.

## Pourquoi faire des coinjoins sur Bitcoin ?
Un des problèmes initiaux à tout système de paiement pair-à-pair est la double dépense : comment empêcher des individus mal intentionnés de dépenser à plusieurs reprises les mêmes unités monétaires sans faire appel à une autorité centrale pour arbitrer ?

Satoshi Nakamoto a apporté une solution à ce dilemme au travers du protocole Bitcoin, un système de paiement électronique pair-à-pair qui fonctionne indépendamment de toute autorité centrale. Dans son livre blanc, il souligne que la seule manière de certifier l'absence de double dépense est d'assurer la visibilité de toutes les transactions au sein du système de paiement.

Afin de garantir que chaque participant soit au courant des transactions, ces dernières doivent être publiquement divulguées. Le fonctionnement de Bitcoin repose donc sur une infrastructure transparente et distribuée, permettant à tout opérateur de nœud de vérifier l'intégralité des chaînes de signatures électroniques et l'historique de chaque pièce, depuis sa création par un mineur.

La nature transparente et distribuée de la blockchain de Bitcoin signifie que tout utilisateur du réseau peut suivre et analyser les transactions de tous les autres participants. En conséquence, l'anonymat au niveau des transactions est impossible. Cependant, l'anonymat est préservé au niveau de l'identification des individus. Contrairement au système bancaire classique où chaque compte est lié à une identité personnelle, sur Bitcoin, les fonds sont associés à des paires de clés cryptographiques, offrant ainsi aux utilisateurs une forme de pseudonymat derrière des identifiants cryptographiques.

Ainsi, la confidentialité sur Bitcoin est mise à mal lorsque des observateurs extérieurs parviennent à associer des UTXO spécifiques à des utilisateurs identifiés. Une fois cette association établie, il devient possible de tracer leurs transactions et d'analyser l'historique de leurs bitcoins. Le coinjoin est justement une technique développée pour casser la traçabilité des UTXO, offrant ainsi une certaine couche de confidentialité aux utilisateurs de Bitcoin au niveau des transactions.

## Comment fonctionne Whirlpool ?
Whirlpool se distingue des autres méthodes de coinjoin par l'utilisation de transactions "_ZeroLink_", qui assurent qu'il n'y a strictement aucun lien technique possible entre tous les inputs et tous les outputs. Ce mixage parfait est obtenu grâce à une structure où chaque participant contribue avec un montant identique en input (à l'exception des frais de minage), générant ainsi des outputs de montants parfaitement égaux.

Cette approche restrictive sur les inputs confère aux transactions coinjoin de Whirlpool une caractéristique unique : l'absence totale de liens déterministes entre les inputs et les outputs. Autrement dit, chaque output possède une probabilité égale d'être attribué à n'importe quel participant, par rapport à tous les autres outputs de la transaction.

Initialement, le nombre de participants à chaque coinjoin Whirlpool était limité à 5, avec 2 nouveaux entrants et 3 remixeurs (nous expliquerons ces concepts plus loin). Toutefois, l'augmentation des frais de transaction on-chain observée en 2023 a incité les équipes de Samourai à repenser leur modèle pour améliorer la confidentialité tout en réduisant les coûts. Ainsi, en tenant compte de la situation du marché des frais et du nombre de participants, le coordinateur peut désormais organiser des coinjoins incluant 6, 7 ou 8 participants. Ces sessions améliorées sont désignées sous le nom de "_Surge Cycles_". Il est important de noter que, quelle que soit la configuration, il y a toujours uniquement 2 nouveaux entrants dans les coinjoins Whirlpool.

Ainsi, les transactions Whirlpool se caractérisent par un nombre identique d'inputs et d'outputs, pouvant être de :
- 5 inputs et 5 outputs ;
![coinjoin](assets/fr/2.webp)
- 6 inputs et 6 outputs ;
![coinjoin](assets/fr/3.webp)
- 7 inputs et 7 outputs ;
![coinjoin](assets/fr/4.webp)
- 8 inputs et 8 outputs.
![coinjoin](assets/fr/5.webp)
Le modèle proposé par Whirlpool est ainsi basé sur de petites transactions coinjoin. À la différence de Wasabi et JoinMarket, où la robustesse des anonsets repose sur le volume de participants sur un cycle unique, Whirlpool mise sur l'enchaînement de plusieurs cycles de petite taille.

Dans ce modèle, l'utilisateur s'acquitte des frais uniquement lors de son entrée initiale dans une pool, lui permettant ensuite de participer à une multitude de remixages sans frais supplémentaires. Ce sont les nouveaux entrants qui prennent en charge les frais de minage pour les remixeurs.

À chaque coinjoin supplémentaire auquel participe une pièce, ainsi que ses pairs rencontrés par le passé, les anonsets vont croître exponentiellement. L'objectif est donc de profiter de ces remixages gratuits qui, à chaque occurrence, contribuent à renforcer la densité des anonsets associés à chaque pièce mixée.

Whirlpool a été conçu en prenant en compte deux exigences importantes :
- L'accessibilité de l'implémentation sur appareils mobiles, étant donné que Samourai Wallet est avant tout une application de smartphone ;
- La rapidité des cycles de remixage pour favoriser une augmentation significative des anonsets.

Ces impératifs ont guidé les choix des développeurs de Samourai Wallet dans la conception de Whirlpool, les amenant à restreindre les participants à un nombre limité par cycle. Un nombre trop restreint aurait compromis l'efficacité du coinjoin, réduisant drastiquement les anonsets générés à chaque cycle, tandis qu'un nombre trop important aurait posé des problèmes de gestion sur les applications mobiles et aurait entravé le flux de cycles.

**Finalement, nul besoin d'avoir un nombre élevé de participants par coinjoin sur Whirlpool puisque les anonsets se font sur l'accumulation de plusieurs cycles de coinjoins.**

[-> En savoir plus sur les anonsets Whirlpool.](https://planb.network/tutorials/privacy/wst-anonsets)

### Les pools et les frais de coinjoin
Pour que ces multiples cycles permettent bien de faire augmenter les anonsets des pièces mixées, il faut mettre un certain cadre afin de restreindre les montants des UTXO utilisés. Whirlpool définit ainsi différentes pools.

Une pool représente un ensemble d'utilisateurs souhaitant mixer ensemble, qui s'accorde sur le montant des UTXO à utiliser pour optimiser le processus de coinjoin. Chaque pool spécifie un montant fixe pour l'UTXO, auquel l'utilisateur doit se conformer pour y participer. Ainsi, pour faire des coinjoins avec Whirlpool, il vous faut sélectionner une pool. Les pools disponibles à l'heure actuelle sont les suivantes :
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

Comme mentionné précédemment, un UTXO est considéré comme appartenant à une pool lorsqu'il est prêt à être intégré dans un coinjoin. Cela ne signifie toutefois pas que l'utilisateur en perd la possession. **À travers les différents cycles de mixage, vous conservez intégralement le contrôle de vos clés et, par conséquent, de vos bitcoins.** C'est d'ailleurs ce qui différencie la technique du coinjoin des autres techniques de mixages centralisés.

Pour entrer dans une pool de coinjoin, il faut régler des frais de service ainsi que des frais de minage. Les frais de service sont fixes pour chaque pool et sont destinés à rémunérer les équipes en charge du développement et de la maintenance de Whirlpool. 

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

Outre les frais de service, les frais de minage propres à toute transaction Bitcoin doivent également être pris en compte. En tant qu'utilisateur de Whirlpool, vous serez tenu de payer les frais de minage de la transaction de préparation (`Tx0`) ainsi que ceux du premier coinjoin. Tous les remixages ultérieurs seront gratuits, grâce au modèle de Whirlpool qui repose sur le paiement de nouveaux entrants.

En effet, dans chaque coinjoin Whirlpool, deux utilisateurs parmi les inputs sont des nouveaux entrants. Les autres inputs proviennent de remixeurs. De ce fait, les frais de minage pour l'ensemble des participants de la transaction sont pris en charge par ces deux nouveaux participants, qui pourront ensuite bénéficier, eux aussi, de remixages gratuits :
![coinjoin](assets/fr/6.webp)
Grâce à ce système de frais, Whirlpool se différencie réellement des autres services de coinjoin puisque les anonsets des UTXO ne sont pas proportionnels au prix payé par l'utilisateur. Ainsi, il est possible d'atteindre des niveaux d'anonymat considérablement élevés en ne s'acquittant que des frais d'entrée de la pool et des frais de minage pour deux transactions (la `Tx0` et le mix initial).

Il est important de noter que l'utilisateur devra également prendre en charge les frais de minage pour retirer ses UTXO de la pool après avoir réalisé ses multiples coinjoins, sauf s'il a sélectionné l'option `mix to`, dont nous parlerons dans le tutoriel ci-dessous.

### Les comptes du portefeuille HD utilisés par Whirlpool
Pour réaliser un coinjoin via Whirlpool, le portefeuille doit générer plusieurs comptes distincts. Un compte, dans le contexte d'un portefeuille HD (*Hierarchical Deterministic*), constitue une section entièrement isolée des autres, cette séparation intervenant au niveau de la troisième profondeur de hiérarchie du portefeuille, c'est-à-dire au niveau des `xpub`.

Un portefeuille HD peut théoriquement dériver jusqu'à `2^(32/2)` comptes différents. Le compte initial, utilisé par défaut sur tous les portefeuilles Bitcoin, correspond à l'index `0'`.

Pour les portefeuilles adaptés à Whirlpool, tels que Samourai ou Sparrow, 4 comptes sont utilisés pour répondre aux besoins du processus de coinjoin :
- Le compte **dépôt**, identifié par l'index `0'` ;
- Le compte **bad bank** (ou doxxic change), identifié par l'index `2 147 483 644'` ;
- Le compte **premix**, identifié par l'index `2 147 483 645'` ;
- Le compte **postmix**, identifié par l'index `2 147 483 646'`.

Chacun de ces comptes remplit une fonction particulière dans le cadre du coinjoin.

Tous ces comptes sont liés à une unique graine (seed), ce qui permet à l'utilisateur de récupérer l'accès à l'ensemble de ses bitcoins en utilisant sa phrase de récupération et, le cas échéant, sa passphrase. Il est cependant nécessaire de préciser au logiciel, lors de cette opération de récupération, les différents index de comptes qui ont été utilisés.

Voyons maintenant les différentes étapes d'un coinjoin Whirlpool au sein de ces comptes.

### Les différentes étapes des coinjoins sur Whirlpool
**Étape 1 : La Tx0**
Le point de départ de tout coinjoin Whirlpool est le compte **dépôt**. Ce compte est celui que vous utilisez automatiquement lorsque vous créez un nouveau portefeuille Bitcoin. Ce compte devra être crédité des bitcoins que l'on souhaite mixer.

La `Tx0` représente la première étape du processus de mixage de Whirlpool. Elle vise à préparer et à égaliser les UTXO pour le coinjoin, en les divisant en unités correspondant au montant de la pool sélectionnée, afin d'assurer l'homogénéité du mixage. Les UTXO ainsi égalisés sont ensuite envoyés vers le compte **premix**. Quant à la différence ne pouvant pas entrer dans la pool, elle est séparée sur un compte spécifique : le **bad bank** (ou "doxxic change").

Cette transaction initiale `Tx0` sert aussi à régler les frais de service dus au coordinateur du mix. Contrairement aux étapes suivantes, cette transaction n'est pas collaborative ; l'utilisateur doit donc assumer l'intégralité des frais de minage :
![coinjoin](assets/fr/7.webp)

Dans cet exemple d'une transaction `Tx0`, un input de `372 000 sats` issu de notre compte **dépôt** est divisé en plusieurs UTXO en sortie, qui se répartissent comme suit :
- Un montant de `5 000 sats` destiné au coordinateur pour les frais de service, correspondant à l'entrée dans la pool de `100 000 sats` ;
- Trois UTXO préparés pour le mixage, redirigés vers notre compte **premix** et enregistrés auprès du coordinateur. Ces UTXO sont égalisés à `108 000 sats` chacun, afin de couvrir les frais de minage pour leur futur mix initial ;
- Le surplus ne pouvant pas entrer dans la pool, car trop petit, est considéré comme change toxique. Il est envoyé vers son compte spécifique. Ici, ce change s'élève à `40 000 sats` ;
- Enfin, il reste `3 000 sats` qui ne constituent pas un output, mais qui sont les frais de minage nécessaires pour confirmer la `Tx0`.

Par exemple, voici une vraie Tx0 Whirlpool (qui ne provient pas de moi) : [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/fr/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Étape 2 : Le doxxic change**
Le surplus n'ayant pas pu intégrer la pool, ici équivalent à `40 000 sats`, est redirigé vers le compte **bad bank**, également désigné sous le terme de "doxxic change", pour en assurer une séparation stricte avec les autres UTXO du portefeuille.

Cet UTXO est dangereux pour la confidentialité de l'utilisateur, car non seulement il est toujours attaché à son passé, et donc éventuellement à l'identité de son propriétaire, mais en plus, il est noté comme appartenant à un utilisateur qui a fait un coinjoin.

Si cet UTXO est fusionné avec des outputs mixés, ces derniers perdront toute la confidentialité gagnée durant les cycles de coinjoins, notamment à cause de la CIOH (*Common-Input-Ownership-Heuristic*). S'il est fusionné avec d'autres doxxic changes, l'utilisateur risque de perdre en confidentialité puisque cela viendra faire un lien entre les différentes entrées des cycles de coinjoins. Il faut donc le traiter avec prudence. La manière de gérer cet UTXO toxique sera détaillée dans la dernière partie de cet article, et de futurs tutoriels aborderont ces méthodes plus en profondeur sur PlanB Network.

**Étape 3 : Le mix initial**
Après la réalisation de la `Tx0`, les UTXO égalisés sont envoyés sur le compte **premix** de notre portefeuille, prêts à être introduits dans leur premier cycle de coinjoin, également appelé "mix initial". Si, comme dans notre exemple, la `Tx0` génère plusieurs UTXO destinés au mixage, chacun d'entre eux sera intégré dans un coinjoin initial distinct.

Au terme de ces premiers mixes, le compte **premix** sera vide, tandis que nos pièces, ayant acquitté les frais de minage pour ce premier coinjoin, seront ajustées exactement au montant défini par la pool choisie. Dans notre exemple, nos UTXO initiaux de `108 000 sats` auront été réduits à exactement `100 000 sats`.
![coinjoin](assets/fr/8.webp)
**Étape 4 : Les remix**
Après avoir fait le mix initial, les UTXO sont transférés dans le compte **postmix**. Ce compte rassemble les UTXO déjà mixés et ceux en attente de remixage. Lorsque le client Whirlpool est actif, les UTXO situés dans le compte **postmix** sont automatiquement disponibles pour des remixages et seront choisis de manière aléatoire pour participer à ces nouveaux cycles.

Pour rappel, les remixages sont ensuite à 100 % gratuits : aucuns frais de service additionnels ou frais de minage ne sont requis. Conserver les UTXO dans le compte **postmix** maintient donc leur valeur intacte, et améliore en même temps leurs anonsets. Voilà pourquoi il est important de permettre à ces pièces de participer à plusieurs cycles de coinjoins. Cela ne vous coûte strictement rien, et cela permet d'augmenter leurs niveaux d'anonymat.

Lorsque vous décidez de dépenser des UTXO mixés, vous pouvez le faire directement depuis ce compte **postmix**. Il est conseillé de garder les UTXO mixés dans ce compte pour bénéficier de remixages gratuits et pour éviter qu'ils ne quittent le circuit de Whirlpool, ce qui pourrait diminuer leur confidentialité.

Comme nous le verrons dans le tutoriel suivant, il y a également l'option `mix to` qui offre la possibilité d'envoyer automatiquement vos pièces mixées vers un autre portefeuille, tel qu'un cold wallet, après un nombre défini de coinjoins.

Après avoir abordé la théorie, plongeons dans la pratique avec un tutoriel sur l'utilisation de Whirlpool via l'application Android Samourai Wallet, synchronisée avec Whirlpool CLI et GUI sur votre propre Dojo !

## Tutoriel : Coinjoin Whirlpool avec son propre Dojo
Il existe de nombreuses options pour utiliser Whirlpool. Celle que je souhaite vous présenter ici est l'option Samourai Wallet, une application open-source de gestion de portefeuille Bitcoin sur Android, mais cette fois-ci **avec son propre Dojo**.

Effectuer des coinjoins via Samourai Wallet en utilisant son propre Dojo est, à mon avis, la stratégie la plus efficace pour réaliser des coinjoins sur Bitcoin à ce jour. Cette approche demande un certain investissement initial en termes de configuration, mais une fois mise en place, elle offre la possibilité de mixer et remixer vos bitcoins en continu, 24 heures sur 24, 7 jours sur 7, sans nécessité de garder votre application Samourai active en permanence. En effet, grâce à Whirlpool CLI opérant sur un nœud Bitcoin, vous restez en permanence prêt à participer à des coinjoins. L'application Samourai vous donne ensuite la possibilité de dépenser vos fonds mixés à tout moment, où que vous soyez, depuis votre smartphone. De plus, cette méthode a l'avantage de ne jamais vous connecter au serveur géré par l'équipe de Samourai, préservant ainsi vos `xpub` de toute exposition externe.

Cette technique est donc idéale pour ceux qui recherchent une confidentialité maximale et des cycles de coinjoins de la plus haute qualité. Néanmoins, elle exige d'avoir à sa disposition un nœud Bitcoin et, comme nous le verrons plus loin, nécessite une certaine mise en place. Elle s'adresse ainsi plutôt à des utilisateurs de niveau intermédiaire à avancé. Pour les débutants, je recommande de se familiariser avec le coinjoin à travers ces deux autres tutoriels, qui présentent comment en faire depuis Sparrow Wallet ou Samourai Wallet (sans Dojo) :
- **[Tutoriel coinjoin Sparrow Wallet](https://planb.network/fr/tutorials/privacy/coinjoin-sparrow-wallet)** ;
- **[Tutoriel coinjoin Samourai Wallet (sans Dojo)](https://planb.network/fr/tutorials/privacy/coinjoin-samourai-wallet)**.

### Comprendre le setup
Pour commencer, vous allez avoir besoin d'un Dojo ! Dojo est une implémentation de nœud Bitcoin basée sur Bitcoin Core, développée par les équipes de Samourai. 

Pour faire tourner votre propre Dojo, vous avez la possibilité soit d'[installer un nœud Dojo de façon autonome](https://samouraiwallet.com/dojo), soit de profiter de Dojo au sein d'une autre solution de nœud Bitcoin "node-in-box". À l'heure actuelle, les options disponibles sont :
- [RoninDojo](https://ronindojo.io/), qui est un Dojo agrémenté d'outils supplémentaires, y compris un assistant d'installation et un assistant d'administration. Je détaille la procédure de mise en place et d'utilisation de RoninDojo dans cet autre tutoriel : [RONINDOJO V2](https://planb.network/fr/tutorials/node/ronin-dojo-v2) ;
- [Umbrel](https://umbrel.com/) avec l'application "Samourai Server" ;
- [MyNode](https://mynodebtc.com/) avec l'application "Dojo" ;
- [Nodl](https://www.nodl.eu/) avec l'application "Dojo" ;
- [Citadel](https://runcitadel.space/) avec l'application "Samourai".
![coinjoin](assets/fr/9.webp)
Dans notre configuration, nous interagirons avec trois interfaces distinctes :
- **Samourai Wallet**, qui accueillera notre portefeuille Bitcoin dédié aux coinjoins. Disponible gratuitement et en open-source pour Android, cette application permet de contrôler votre portefeuille de mixage, notamment pour les dépenses de vos postmix depuis votre smartphone ;
- **Whirlpool CLI** (_Command Line Interface_), qui fonctionnera sur le nœud hébergeant le Dojo. Ce logiciel aura accès aux clés de votre portefeuille Samourai. C'est lui qui se chargera de communiquer avec le coordinateur et qui gèrera les coinjoins en continu. Il agit comme une copie de votre portefeuille Samourai sur votre nœud, prête à participer aux coinjoins à tout moment ;
- **Whirlpool GUI** (_Graphical User Interface_), l'interface utilisateur graphique que nous utiliserons pour surveiller l'activité de Whirlpool CLI et initier des mixages à distance. Whirlpool GUI offre une représentation visuelle des opérations menées par Whirlpool CLI. Ce logiciel doit être installé sur un ordinateur séparé du Dojo. Pour les utilisateurs d'Umbrel, MyNode, Nodl, et Citadel, Whirlpool GUI est obligatoire. Cependant, avec RoninDojo, l'interface Whirlpool GUI est déjà intégrée à l'interface web de votre nœud. Vous n'aurez donc pas besoin de l'installer sur un PC séparé.

Selon moi, l'utilisation de RoninDojo représente la meilleure solution pour réaliser des coinjoins avec un Dojo. Puisque ce logiciel de node-in-box est en partenariat direct avec les équipes de Samourai, RoninDojo est bien plus optimisé pour faire cela. De plus, l'intégration de Whirlpool GUI dans l'interface web simplifie considérablement le processus de mise en place. Dans ce tutoriel, je vais tout de même vous expliquer comment faire avec les autres solutions qui intègrent Dojo (Umbrel...).

### Préparer son Dojo
Pour commencer, vous allez devoir installer Dojo et obtenir le QR code ou le lien qui vous permettra de vous y connecter à distance. Ce lien est une adresse Tor se terminant par `.onion`. Si vous utilisez RoninDojo, il vous suffira de naviguer vers le menu `Pairing` pour accéder à ces informations.

![coinjoin](assets/fr/10.webp)

En dessous de `Samourai Dojo`, cliquez sur le bouton `Pair now`.

![coinjoin](assets/fr/11.webp)

Votre QR code de connexion et le lien correspondant s'afficheront.

![coinjoin](assets/fr/12.webp)

Si vous êtes sur Umbrel, rendez-vous dans l'App Store et recherchez l'application `Samourai Server`. Elle se trouve dans l'onglet `Bitcoin`.

![coinjoin](assets/fr/13.webp)

Installez l'application.

![coinjoin](assets/fr/14.webp)

En ouvrant l'application, vous aurez ensuite accès au QR code de connexion à votre Dojo.

![coinjoin](assets/fr/15.webp)

Si vous utilisez un autre logiciel de node-in-box tel que MyNode, Citadel ou Nodl, le processus est semblable à celui d'Umbrel. Il faut installer l'application Samourai ou Dojo afin d'obtenir les informations nécessaires pour se connecter à votre Dojo.

![coinjoin](assets/fr/16.webp)

### Préparer son portefeuille Samourai Wallet
Après avoir récupéré les informations de connexion à votre Dojo, il est maintenant temps de configurer votre portefeuille pour les coinjoins. Deux cas de figure se présentent : si vous n'avez pas encore de portefeuille Samourai Wallet sur votre smartphone, la démarche est simple, il suffit d'en créer un nouveau. Cependant, si vous possédez déjà un portefeuille Samourai Wallet, vous devrez réinstaller l'application pour pouvoir y associer un nouveau Dojo. Cette étape est nécessaire, car la connexion à un Dojo ne peut être établie qu'au premier lancement de l'application. Néanmoins, grâce au fichier de sauvegarde chiffré automatiquement généré par Samourai sur votre téléphone, cette procédure est simple et rapide.

*Si vous n'avez jamais utilisé Samourai, vous pouvez ignorer ces étapes préliminaires et procéder directement à l'installation de l'application.*

Avant toute chose, assurez-vous que votre application Samourai Wallet est bien à jour. Pour ce faire, consultez le Google Play Store ou bien comparez la version de votre application dans `Settings > Other` avec celle disponible [sur le site de Samourai](https://samouraiwallet.com/download).

![coinjoin](assets/fr/17.webp)

Assurez-vous d'être en possession de la phrase de récupération de votre portefeuille Samourai et vérifiez qu'elle est bien lisible. Puis, procédez à un test de votre passphrase BIP39 en naviguant dans `Settings > Troubleshoot > Passphrase/Backup test` pour confirmer son exactitude.

![coinjoin](assets/fr/18.webp)

Entrez votre passphrase, puis vérifiez que Samourai vous confirme bien la validité de celle-ci. 

![coinjoin](assets/fr/19.webp)

Si votre passphrase est invalide, ou si vous ne possédez pas votre phrase de récupération, il est impératif de stopper immédiatement la procédure ! **Vous risquez de perdre vos bitcoins lors de cette opération.** Dans ce cas, il est conseillé de transférer vos fonds dans un autre portefeuille et de démarrer avec un nouveau portefeuille vierge. Les étapes suivantes sont à suivre uniquement si vous êtes certain de détenir toutes les informations de sauvegarde nécessaires et que votre passphrase est valide.

Poursuivez ensuite avec la création d'une sauvegarde chiffrée de votre portefeuille et copiez-la dans votre presse-papiers. Pour réaliser cette opération, cliquez sur les trois petits points situés en haut à droite de l'écran, puis sélectionnez `Export wallet backup`.

![coinjoin](assets/fr/20.webp)

**À partir de cette étape, ne copiez plus rien dans votre presse-papier !** Il faut absolument que vous conserviez votre sauvegarde copiée.

Si vous avez correctement exécuté les étapes précédentes, vous êtes à présent en mesure de supprimer votre portefeuille Samourai en toute sécurité. Pour cela, dirigez-vous dans : `Settings > Wallet > Secure erase the wallet`.

![coinjoin](assets/fr/21.webp)

![coinjoin](assets/fr/22.webp)

*Si vous n'avez jamais utilisé Samourai et que vous installez l'application de zéro, vous pouvez reprendre le tuto à cette étape.* 

Votre application Samourai est désormais réinitialisée. Ouvrez l'application et procédez aux étapes de configuration comme si vous l'utilisiez pour la première fois.

![coinjoin](assets/fr/23.webp)

À l'étape suivante, vous accéderez à la page dédiée à la configuration de votre Dojo. Sélectionnez l'option `Dojo`, puis saisissez les informations de connexion de votre Dojo. Pour ce faire, vous avez la possibilité de scanner les informations en appuyant sur `Scan QR`.

![coinjoin](assets/fr/24.webp)

*Pour les nouveaux utilisateurs de Samourai, il sera nécessaire de créer un portefeuille à partir de zéro. Si vous avez besoin d'assistance, vous pouvez consulter les instructions pour configurer un nouveau portefeuille Samourai [dans ce tutoriel, spécifiquement dans la section « Créer un portefeuille logiciel »](https://planb.network/tutorials/privacy/coinjoin-samourai-wallet).*

Si vous procédez à la restauration d'un portefeuille Samourai déjà existant, sélectionnez `Restore existing wallet`, puis choisissez `I have a Samourai backup file`.

![coinjoin](assets/fr/25.webp)

Normalement, vous devriez toujours avoir votre fichier de récupération dans votre presse-papiers. Cliquez alors sur `PASTE` pour insérer votre fichier dans l'emplacement dédié. Afin de le déchiffrer, il sera également nécessaire de saisir la passphrase BIP39 de votre portefeuille dans le champ correspondant, situé juste en dessous. Pour terminer, cliquez sur `FINISH`.

![coinjoin](assets/fr/26.webp)

Vous serez alors redirigé vers votre portefeuille Samourai Wallet qui, cette fois, sera connecté à votre propre Dojo.

![coinjoin](assets/fr/27.webp)

### Installation de Whirlpool GUI
Il est maintenant temps d'installer Whirlpool GUI, l'interface utilisateur graphique qui vous permettra de gérer vos cycles de coinjoins depuis votre PC habituel. Pour les utilisateurs de RoninDojo, cette étape n'est pas nécessaire puisque la gestion des coinjoins peut s'effectuer directement via l'interface web dans `Apps > Whirlpool`. En revanche, si vous utilisez une autre solution de nœud Bitcoin "node-in-box", il est impératif de procéder à cette installation.
![coinjoin](assets/fr/28.webp)
Rendez-vous sur votre ordinateur personnel et [téléchargez le logiciel Whirlpool depuis le site officiel de Samourai Wallet](https://samouraiwallet.com/download/whirlpool), en sélectionnant la version qui correspond à votre système d'exploitation.

![coinjoin](assets/fr/29.webp)

Avant de lancer Whirlpool GUI, il est nécessaire d'installer JAVA 8 ou une version supérieure sur votre machine. Pour cela, [vous pouvez installer OpenJDK](https://adoptium.net/).
![coinjoin](assets/fr/30.webp)
Il est également nécessaire d'avoir Tor Daemon ou Tor Browser opérationnels en arrière-plan sur votre ordinateur. Assurez-vous de démarrer Tor avant chaque session d'utilisation de Whirlpool GUI. Si Tor n'est pas encore installé sur votre machine, [vous pouvez le télécharger et l'installer depuis le site officiel du projet Tor](https://www.torproject.org/download/), puis veillez à le lancer fond.

![coinjoin](assets/fr/31.webp)

Une fois JDK installé sur votre système et Tor lancé en fond, vous pouvez démarrer Whirlpool GUI.

![coinjoin](assets/fr/32.webp)

Depuis Whirlpool GUI, cliquez sur `Advanced: Remote CLI` pour connecter votre Whirlpool CLI qui est sur votre Dojo. Vous allez avoir besoin de l'adresse Tor de votre Whirlpool CLI. 

![coinjoin](assets/fr/33.webp)

Pour localiser votre adresse Tor sur Umbrel et d'autres solutions "node-in-box", il suffit de démarrer l'application Samourai Server ou Dojo (le nom peut varier selon le logiciel utilisé). L'adresse Tor sera visible directement sur la page de l'application.
![coinjoin](assets/fr/34.webp)
Dans Whirlpool GUI, saisissez l'adresse Tor que vous avez obtenue précédemment dans le champ `CLI address`. Conservez le préfixe `http://`, mais ne mettez pas le port `:8899` à la fin. Collez uniquement l'adresse telle qu'elle vous a été fournie.

![coinjoin](assets/fr/35.webp)

Dans le champ Tor Proxy, inscrivez `socks5://127.0.0.1:9050` si vous utilisez Tor Daemon, ou `socks5://127.0.0.1:9150` si c'est Tor Browser. Lors de votre première connexion à Whirlpool CLI via Whirlpool GUI, il est possible de laisser vide le champ de la clé API. Si ce n'est pas votre première connexion, veuillez entrer votre clé API dans l'espace dédié. Cette clé peut être localisée sur la même page que votre adresse Tor.

![coinjoin](assets/fr/36.webp)

Une fois que vous avez tout renseigné, cliquez sur le bouton `Connect`. Patientez, la connexion peut prendre quelques minutes.

![coinjoin](assets/fr/37.webp)

### Appairer son portefeuille Samourai Wallet à Whirlpool GUI 
*Pour les utilisateurs de RoninDojo, vous pouvez reprendre le tutoriel ici.*

Nous allons maintenant appairer le portefeuille Samourai que nous avons configuré précédemment avec le logiciel Whirlpool GUI, ou bien directement avec RoninDojo pour ceux qui utilisent ce logiciel. Que vous utilisiez Whirlpool GUI ou RoninDojo, il vous sera demandé de coller ou de scanner les informations d'appairage de votre portefeuille Samourai.

![coinjoin](assets/fr/38.webp)

Pour trouver ces informations, rendez-vous dans les paramètres de votre portefeuille.

![coinjoin](assets/fr/39.webp)

Cliquez sur `Transactions`, puis sur `Pair to Whirlpool GUI`.

![coinjoin](assets/fr/40.webp)

Samourai vous fournira alors les informations nécessaires pour établir la connexion. Attention, ces données sont sensibles ! Vous pouvez les transférer vers votre PC soit en les copiant directement, soit en scannant le QR code affiché, en utilisant la webcam de votre ordinateur après avoir cliqué sur le symbole du QR code.

![coinjoin](assets/fr/41.webp)

Après avoir effectué cette opération, dans Whirlpool GUI, sélectionnez `Initialize GUI`. Veuillez patienter, car cette étape peut prendre un moment.

![coinjoin](assets/fr/42.webp)

Que vous utilisiez Whirlpool GUI ou RoninDojo, il vous sera demandé de saisir la passphrase de votre portefeuille Samourai. Insérez-la dans le champ dédié, puis appuyez sur le bouton `Login` pour poursuivre.

![coinjoin](assets/fr/43.webp)

Vous arriverez ensuite sur la page d'accueil de Whirlpool CLI

![coinjoin](assets/fr/44.webp)

### Lancer les coinjoins depuis Whirlpool GUI 
*Pour les utilisateurs de RoninDojo, le processus à suivre est identique. L'interface de l'application Whirlpool intégrée dans RoninDojo offre les mêmes options et fonctionnalités que le logiciel Whirlpool GUI sur desktop. Vous pouvez donc suivre ces instructions de la même façon.*

Maintenant que tout est configuré, vous êtes prêt à commencer le mixage de vos bitcoins. Pour cela, transférez les bitcoins que vous souhaitez mixer vers le compte **Dépôt** de votre portefeuille Samourai Wallet. Cette opération peut être réalisée soit directement via l'application Samourai Wallet, soit sur Whirlpool GUI. À partir de la page principale, cliquez sur le bouton `+ Deposit` situé en haut à gauche.

![coinjoin](assets/fr/45.webp)

Whirlpool GUI générera une adresse de réception. Il vous affichera également le montant minimum nécessaire pour participer à chaque pool de coinjoin. Ce montant varie en fonction du marché de frais. Il est conseillé de déposer un montant légèrement supérieur au minimum requis, car si les frais de minage ne diminuent pas, votre UTXO pourrait ne pas être accepté dans la pool désirée. Envoyez donc vos bitcoins à l'adresse fournie. Pour obtenir une nouvelle adresse, il suffit de cliquer sur le bouton `Renew address`.

![coinjoin](assets/fr/46.webp)

Une fois le dépôt confirmé, vous pourrez le voir apparaitre dans le compte **Deposit** sur Whirlpool GUI. 

![coinjoin](assets/fr/47.webp)

Pour lancer les cycles de coinjoins, sélectionnez les UTXO que vous souhaitez mixer et appuyez sur le bouton `Premix`. Faites attention : si vous sélectionnez plusieurs UTXO différents en même temps, ils seront regroupés lors de la transaction de préparation `TX0`. Cette fusion peut entraîner une diminution de la confidentialité, surtout si les UTXO proviennent de sources variées, à cause de la CIOH (*Common Input Ownership Heuristic*).

![coinjoin](assets/fr/48.webp)

La page de configuration de Whirlpool s'ouvre. Vous pouvez choisir la pool dans laquelle vous désirez entrer. Sélectionnez également les frais de minage dédiés à la `TX0` et aux premiers coinjoins. En bas de cette page, un résumé vous présentera le montant du doxxic change ainsi que le montant et le nombre d'UTXO qui seront égalisés et inclus dans les cycles de coinjoins. Si vous êtes satisfait de cette configuration, appuyez sur le bouton `Premix` pour commencer les cycles de coinjoins.
![coinjoin](assets/fr/49.webp)

Une fois la `TX0` créée, vous pourrez voir vos UTXO égalisés dans le compte **Premix**, en attente de confirmation. Pour permettre à vos pièces de se remixer automatiquement 24 heures sur 24 et 7 jours sur 7, je vous recommande d'activer l'option `Automatically mix premix & postmix`. Vous trouverez cette fonctionnalité dans l'onglet `Configuration`, situé à gauche de votre fenêtre Whirlpool GUI.

![coinjoin](assets/fr/50.webp)

Après avoir démarré les coinjoins, vous pouvez quitter Whirlpool GUI ainsi que Samourai Wallet. Seul votre nœud doit rester connecté pour pouvoir participer à des coinjoins en continu. Néanmoins, il convient de vérifier périodiquement l'état d'avancement de vos cycles coinjoins. Si vous constatez que vos UTXO ne sont plus sélectionnés pour un coinjoin depuis un certain temps, cela peut indiquer un bug. Dans ce cas, accédez à Whirlpool CLI et sélectionnez `Start` pour réactiver vos cycles de coinjoins.

![coinjoin](assets/fr/51.webp)

Vos UTXO mixés sont visibles depuis le compte **Postmix** sur Whirlpool GUI. De plus, vous avez la possibilité de les consulter et de les dépenser directement via l'interface Whirlpool sur Samourai Wallet. Pour accéder à ce menu, cliquez sur le `+` bleu situé en bas de votre écran, puis sélectionnez `Whirlpool`.

![coinjoin](assets/fr/52.webp)

Les comptes Whirlpool sont facilement identifiables sur Samourai Wallet par leur couleur bleue. Vous avez ainsi la liberté de dépenser vos UTXO mixés depuis n'importe quel lieu et à tout moment.

![coinjoin](assets/fr/53.webp)

Afin de suivre vos mixages automatiques, je vous conseille également de configurer un portefeuille watch-only via l'application Sentinel. Intégrez la ZPUB de votre compte **Postmix** et surveillez en temps réel le progrès de vos cycles de coinjoins. Si vous souhaitez comprendre comment utiliser Sentinel, je vous recommande de consulter cet autre tutoriel : [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/sentinel).