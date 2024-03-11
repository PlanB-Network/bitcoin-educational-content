---
name: Coinjoin - Sparrow Wallet
description: Comment faire un coinjoin sur Sparrow Wallet ?
---
![cover](assets/cover.webp)

Dans ce tutoriel, vous allez apprendre ce qu'est un coinjoin et comment en faire grâce au logiciel Sparrow Wallet et l'implémentation Whirlpool.

## Qu'est-ce qu'un coinjoin sur Bitcoin ?
**Le coinjoin est une technique qui permet de casser le traçage des bitcoins sur la blockchain**. Il repose sur une transaction collaborative à la structure spécifique de même nom : la transaction coinjoin.

Les transactions coinjoin renforcent la confidentialité des utilisateurs de Bitcoin en complexifiant l'analyse de chaîne pour les observateurs externes. Leur structure permet de fusionner plusieurs pièces de différents utilisateurs en une unique transaction, brouillant ainsi les pistes et rendant difficile la détermination des liens entre les adresses d'entrée et de sortie.

Le principe du coinjoin repose sur une approche collaborative : plusieurs utilisateurs qui souhaitent mélanger leurs bitcoins déposent des montants identiques en entrées d'une même transaction. Ces montants sont ensuite redistribués en sorties de valeur équivalente. À l'issue de la transaction, il devient impossible d'associer un output spécifique à un utilisateur donné. Aucun lien direct n'existe entre les entrées et les sorties, rompant ainsi l'association entre les utilisateurs et leurs UTXO, de même que l'historique de chaque pièce.
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
Contrairement aux autres implémentations de coinjoin, Whirlpool se démarque par la construction de transactions « ZeroLink », c'est-à-dire avec strictement aucun lien technique possible entre tous les inputs et tous les outputs. Ce mixage parfait est rendu possible par une transaction coinjoin où chaque utilisateur dépose un même montant en input (modulo les frais de minage), qui ressortent en autant d'outputs de même montant.

Avec ce type de construction restrictive sur les inputs, la transaction coinjoin de Whirlpool est la seule qui permette aux utilisateurs de disposer de 0 % de liens déterministes entre les inputs et les outputs. Cela signifie que chaque output a parfaitement la même probabilité d'appartenir à un utilisateur que tous les autres outputs de la transaction.

Le nombre de participants à chaque mix Whirlpool était historiquement limité à 5, avec 2 entrants et 3 remixeurs (nous découvrirons plus loin en quoi cela consiste). Mais les gros pics de frais on-chain que l'on a connu en 2023 ont poussé les équipes de Samourai a optimiser leur modèle pour gagner plus de confidentialité tout en utilisant moins de frais. Dorénavant, en fonction de l'état du marché de frais et des entrants, le coordinateur peut également choisir de faire également des coinjoins avec 6, 7 ou 8 participants. Ces nouveaux coinjoins Whirlpool sont appelés « *Surge Cycles* ». Dans tous les cas, il n'y a toujours que 2 entrants dans les coinjoins Whirlpool.

Ainsi, les transactions Whirlpool se caractérisent par un nombre identique d'inputs et d'outputs, pouvant être de :
- 5 inputs et 5 outputs ;
![coinjoin](assets/fr/2.webp)
- 6 inputs et 6 outputs ;
![coinjoin](assets/fr/3.webp)
- 7 inputs et 7 outputs ;
![coinjoin](assets/fr/4.webp)
- 8 inputs et 8 outputs.
![coinjoin](assets/fr/5.webp)
Le modèle proposé par Whirlpool est ainsi basé sur de petites transactions coinjoin. Contrairement à Wabisabi et à JoinMarket, la force des anonsets n'est pas acquise par le nombre d'utilisateurs participant à un seul cycle, mais par la succession de plusieurs petits cycles de coinjoins.

L'utilisateur sera amené à payer les frais une seule fois, lors de son entrée dans une pool, puis il pourra gratuitement remixer autant qu'il le souhaite. Ce sont les nouveaux entrants qui paient les frais de minage pour les remixeurs.

Les anonsets viendront augmenter de façon exponentielle au fur et à mesure des remixes de l'utilisateur et de ses pairs rencontrés. L'objectif est donc de profiter au maximum de tous ces remixes gratuits qui viennent à chaque fois ajouter de la profondeur aux anonsets de la pièce mixée.

Whirlpool a été imaginé selon 2 critères principaux :
- Que l'implémentation soit utilisable sur mobile puisque Samourai est une application ;
- Que les cycles de remixes se fassent rapidement afin de soutenir l'augmentation des anonsets.

Ce sont pour ces deux raisons que les équipes de Samourai Wallet, qui ont développé Whirlpool, ont choisi de limiter le nombre d'utilisateurs à quelques utilisateurs par cycle. Un nombre plus faible n'aurait pas permis un coinjoin assez efficace et serait venu réduire trop fortement les anonsets par cycle. Un nombre trop élevé n'aurait sûrement pas été gérable sur des clients mobiles, et il serait venu réduire le flux de cycles.

Finalement, nul besoin d'avoir un nombre élevé de participants par coinjoin sur Whirlpool puisque les anonsets se font sur l'accumulation de plusieurs cycles de mixage.

[-> En savoir plus sur les anonsets Whirlpool.](https://planb.network/tutorials/privacy/wst-anonsets)

### Les pools et les frais de coinjoin
Pour que ces multiples cycles permettent bien de faire augmenter les anonsets des pièces mixées, il faut mettre un certain cadre afin de restreindre les montants des UTXO utilisés. Whirlpool défini ainsi différentes pools.

Une pool est un groupement d'utilisateurs souhaitant mixer, qui se sont entendus sur le montant des UTXO utilisés afin d'optimiser le fonctionnement du coinjoin. Chaque pool définit un montant fixe de l'UTXO auquel l'utilisateur doit s'adapter pour pouvoir y entrer. Concrètement, lorsque vous souhaitez réaliser des coinjoins Whirlpool, vous devez choisir une pool dans laquelle entrer pour commencer à mixer. Les différentes pools existantes sur Whirlpool actuellement sont :
- 0,5 bitcoins ;
- 0,05 bitcoin ;
- 0,01 bitcoin ;
- 0,001 bitcoin (= 100 000 sats).

Lorsque vous rentrez dans une pool avec une pièce, celle-ci va être divisée pour pouvoir produire des UTXO parfaitement homogènes avec les autres pièces de la pool. Il existe toutefois une limite maximale pour chaque pool. Cela signifie qu'au dessus ce montant, vous devrez soit faire 2 entrées différentes dans la pool, soit choisir la pool supérieure :

| Pool (bitcoin) | Montant maximum par entrée (bitcoin) |
|----------------|--------------------------------------|
| 0,5            | 35                                   |
| 0,05           | 3,5                                  |
| 0,01           | 0,7                                  |
| 0,001          | 0,025                                |
Pour entrer dans une pool de coinjoin, il faut régler des frais de service ainsi que des frais de minage. Les frais de service sont fixes pour chaque pool et sont destinés aux équipes qui développent et gèrent Whirlpool afin de les rémunérer pour ce service. Si vous utilisez Sparrow Wallet, les équipes de Samourai rétrocèdent ces frais aux développeurs de Sparrow. 

Les frais de Whirlpool sont uniquement payés une fois lorsque vous accédez à la pool. Une fois entré dans une pool, vous pourrez gratuitement remixer autant de fois que vous le souhaitez. Actuellement, voici les frais fixes pour chaque pool :

| Pool (bitcoin) | Frais d'entrée (bitcoin)        |
|----------------|---------------------------------|
| 0,5            | 0,0175                          |
| 0,05           | 0,00175                         |
| 0,01           | 0,0005 (50 000 sats)            |
| 0,001          | 0,00005 (5 000 sats)            |
Notez également que ces frais sont un peu comme un ticket d'entrée pour la pool. Ainsi, que vous entriez dans la pool 0,01 avec 0,01 btc, ou avec 0,5 btc, les frais seront exactement les mêmes. 

Avant de mixer, un utilisateur doit donc se demander s'il souhaite payer moins de frais avec une petite pool, auquel cas, il ressortira avec plusieurs petits UTXO, ou bien s'il préfère utiliser une plus grosse pool en payant plus de frais, mais en ressortant avec moins d'UTXO. A la sortie des différents cycles de coinjoins, il est généralement déconseillé de fusionner ensemble plusieurs UTXO mixés. Cette pratique pourrait venir casser la confidentialité gagnée précédemment grâce aux cycles de coinjoins, notamment à cause de la CIOH (*Common-Input-Ownership-Heuristic*) . Alors, il vaut mieux parfois utiliser une plus grosse pool, quitte à payer plus de frais, afin de ressortir avec moins d'UTXO d'une taille plus importante. C'est un choix que l'utilisateur doit faire en considérant les différents compromis.

Les autres frais à considérer seront évidemment les frais de minage inhérents à toute transaction Bitcoin. En tant qu'utilisateur de Whirlpool, vous devrez payer les frais de minage de la Tx0 et les frais de minage du mix initial. Tous les autres remixes seront gratuits pour vous puisque le modèle de frais de Whirlpool est fondé sur les nouveaux entrants.

En effet, dans chaque coinjoin, 2 utilisateurs parmi les inputs sont des entrants. Tous les autres inputs sont issus de remixeurs. Ainsi, les deux entrants de chaque coinjoin paieront les frais de minage pour tous les autres participants de la transaction, puis ces deux entrants pourront à leur tour profiter de la gratuité des remixes suivants.
![coinjoin](assets/fr/6.webp)
Grâce à ce modèle de frais, Whirlpool se différencie réellement des autres services de coinjoin puisque les anonsets des UTXO ne sont pas proportionnels au prix payé par l'utilisateur. On peut donc aboutir à des anonsets très élevés, en ayant simplement payé les frais de la pool, et les frais de minage pour deux transactions (Tx0 et mix initial).

Évidemment, l'utilisateur devra également payer les frais de minage lorsqu'il souhaitera sortir ses UTXO de la pool après avoir effectué ses nombreux remixes, à moins qu'il ait opté pour l'option `mix to` que nous allons découvrir plus loin.

### Les comptes du portefeuille HD utilisés par Whirlpool




### Les différentes étapes des coinjoins sur Whirlpool





## Tutoriel : Whirlpool sur Sparrow Wallet







### Comment connaître la qualité de nos cycles de coinjoin ?




### Comment gérer le doxxic change ?






**Ressources supplémentaires :** 
- [Tutoriel vidéo Sparrow Wallet](https://planb.network/tutorials/wallet/sparrow) ;
- [Tutoriel vidéo Samourai Wallet](https://planb.network/tutorials/wallet/samourai) ;
- [Documentation Samourai Wallet - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts) ;
- [Thread Twitter sur les coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739) ;
- [Article de blog sur les coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin) ;
- [Tutoriel Bitcoin Magazine sur Whirlpool.](https://bitcoinmagazine.com/technical/how-to-whirlpool-bitcoin-sparrow-wallet)
