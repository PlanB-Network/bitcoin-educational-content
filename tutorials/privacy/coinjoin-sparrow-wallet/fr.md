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
![coinjoin](assets/fr/1.png)

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

Le nombre de participants à chaque mix Whirlpool était historiquement limité à 5, avec 2 entrants et 3 remixeurs (nous découvrirons plus tard en quoi cela consiste). 


Toute transaction CoinJoin sur Whirlpool dispose donc toujours de 5 entrées et de 5 sorties.




### Les pools et les frais de coinjoin




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
