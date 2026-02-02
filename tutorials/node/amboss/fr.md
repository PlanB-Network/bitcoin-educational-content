---
name: Amboss
description: Explorez et analysez le Lightning Network
---

![cover](assets/cover.webp)

Le Lightning Network est une couche ajoutée au protocole Bitcoin, principalement conçue pour favoriser l'adoption des paiements quotidiens en Bitcoin. Il permet d'augmenter considérablement la vitesse de traitement de chaque transaction. Fondé sur le principe de la décentralisation, le Lightning Network fonctionne grâce à un réseau de nœuds (des ordinateurs exécutant une implémentation Lightning) communiquant pair-à-pair en se relayant des données (paiements et vérification de paiement).

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Tout comme sur la chaîne principale, il est essentiel de permettre aux utilisateurs d’accéder aux informations et à l'état du réseau. Cela facilite les connexions entre les nœuds et de réduire au maximum les problèmes de liquidités qui se pose fréquents sur le réseau. En effet, sur le Lightning Network, nous privilégions les micro-paiements, dont les montants sont relativement moins conséquent que ceux des transactions sur la chaîne principale de Bitcoin.

Il est important de noter que tous les nœuds du Lightning ne sont pas répertoriés sur la plateforme Amboss.

Au même titre que [Mempool Space](https://mempool.space) qui recense les informations utiles sur la chaîne principale du protocole Bitcoin, depuis 2022, [Amboss](https://amboss.space) vous permet d'avoir des informations sur :

- Les nœuds présents sur le Lightning Network
- Les canaux de paiement et leur capacité de paiement
- L'évolution du Lightning Network au fil du temps
- Les statistiques sur les frais à payer aux nœuds relayeurs de vos paiements.

https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Dans ce tutoriel, nous vous présentons cette plateforme, une ressource essentielle pour tous les utilisateurs du Lightning Network, vous qui souhaitez explorer ses fonctionnalités, et connecter votre nœud pour agrandir le réseau, etc.


## Trouver des paires

L'un des objectifs de la plateforme Amboss est de permettre aux différents nœuds du réseau de se connecter et d'échanger des informations entre eux. Depuis la page d'accueil de la plateforme, vous pouvez directement rechercher le nom d'un nœud que vous connaissez déjà ou retrouver des nœuds des portefeuilles Lightning les plus populaires que vous utilisez.

![home](assets/fr/01.webp)

![wallet](assets/fr/02.webp)

https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Sur la page d'accueil, vous trouverez également les nœuds classés en selon :
- L'évolution de la capacité : la quantité de bitcoin associée à la clé publique du nœud et le total disponible dans l'ensemble de ses canaux.
- L'évolution du nombre de canaux : Le nombre de nouvelles connexions établies avec d'autres nœuds du réseau.
- La popularité du nœud : la fréquence d'utilisation de ce nœud.

![nodes](assets/fr/03.webp)

Choisir un bon nœud auquel se connecter revient donc à vérifier les critères suivants :

- S'assurer que le nœud dispose d'une quantité suffisante de bitcoins ; plus la capacité de ce nœud est grande, plus vous pouvez faire des paiements de montants conséquents.

- S'assurer que le nœud possède un grand nombre de connexions et de canaux ouverts avec les autres nœuds du réseau.

- S'assurer que le nœud est actif et encore apprécié par ses paires en vérifiant le nombre de nouveaux canaux ; plus  ce nœud a de nouveaux canaux ouverts, plus il  est apprécié par les autres nœuds du réseau.

Une fois le nœud idéal identifié, Cliquez sur son nom pour accéder à sa page d'informations.

Sur cette interface, vous pouvez vérifier l'horodatage du dernier canal ouvert, vous avez un indice sur l'activité du nœud. Vous y verrez aussi les détails concernant la capacité ses canaux : cette information est capitale pour vous qui souhaitez utiliser activement ce nœud pour faire vos paiements.


![node_info](assets/fr/04.webp)

Dans la section gauche, vous avez plus de détails concernant la localisation de ce nœud. Vous pouvez consulter par exemple :
- La clé publique : l'identifiant juste en dessous du nom du nœud.
- La position géographique de ce nœud.


![channels](assets/fr/05.webp)

Cette interface vous indique l'adresse de connexion à ce nœud : elle se présente sous forme `pubkey@ip:port`. Dans notre exemple, nous souhaitons nous connecter au nœud dont :
- la clé publique `pubkey` est : `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- l'adresse IP : `170.75.163.209`
- Le port : `9735`

![geoinfo](assets/fr/06.webp)

Dans la section **Canaux**, vous verrez la liste des canaux ouverts ainsi que les connexions du nœud avec les autres nœuds du réseau. Sur cette interface, plusieurs informations essentielles permettent de vérifier si ce nœud correspond à vos besoins et s’il est fiable :

- **Le ratio entrant** : Le montant que le nœud vous facturera pour chaque million de satoshi qu'il recevra, selon le canal utilisé. 
- **Le ratio (parts par million)** : il indique le nombre de satoshi par million d'unités que le nœud prélève lorsque vous faites transiter un paiement via un de ses canaux. Par exemple, si vous envoyez `10_000 sats` via un canal dont le ratio est de `500 ppm` , vous devrez payer au nœud `10_000 * 500 / 1_000_000` satoshis soit l'équivalent de `5 sats`.
-  **Le [HTLC](https://planb.academy/resources/glossary/htlc) maximum** : Le montant maximum que le nœud autorise à faire transiter par l'un de ces canaux.

En consultant le tableau de cette interface, vous pouvez également retrouver toutes ces informations pour chaque nœud auquel vous êtes connecté.

![channels_info](assets/fr/07.webp)

Dans la section **Cartes des canaux**, vous avez une vue d’ensemble des répartitions et de la capacité des différents canaux de ce nœud. Vous pouvez modifier le critère de répartition affiché en sélectionnant l'une des options de la liste déroulante à droite.

![cha_maps](assets/fr/08.webp)

La section des **Canaux fermés** recense tous les anciens canaux du nœud, classés en fonction du type de fermeture :
- Une **fermeture mutuelle** : représente l'accord des deux parties qui signent avec leur clé privée la transaction marquant la fermeture du canal et la répartition des soldes dans ce canal
- Une **fermeture forcée** : représente la fermeture brusque et unilatérale d'une des parties du canal. Ce type de fermeture n'est pas recommandé, car le Lightning Network est un protocole basé sur la punition : lorsque vous essayez de frauder avec le solde d'un canal, vous risquez de perdre tout votre solde disponible dans ce canal.

![closed](assets/fr/09.webp)

Obtenez les informations relatives aux frais de transit pour faire transiter vos paiements dans un canal du nœud que vous utilisez

![fees](assets/fr/10.webp)

## Informations sur le réseau

Amboss ne se focalise pas uniquement sur les informations des membres du réseau mais également sur l'état du réseau en lui-même.

Dans la section **Statistiques**,sous le menu gauche "Simulations", retrouvez le graphique de probabilité de réussite d'un paiement en fonction du montant de ce paiement.

En effet vous constaterez que la courbe est décroissante parce que, plus le montant de votre paiement augmente, moins vous avez de chance de voir ce paiement aboutir. Cela traduit le réel problème de liquidité présent sur le Lightning Network. Par exemple, vous avez environ `79%` de chance que votre paiement de `10_000` satoshis soit effectué. En revanche, pour un paiement de `3_000_000` satoshis vous avez moins de `13%` de chances de réussite.

![network](assets/fr/11.webp)

Le menu **Statistiques réseau** vous permet de retrouver sous forme de graphique les statistiques des : 
- Canaux de paiement 
- Nœuds
- Capacité
- Frais
- Évolution de canaux.

![network_stat](assets/fr/12.webp)

Dans le menu **Statistiques de marché**, l'option **Détails d'ordres** , vous permet de visualiser la demande de liquidité sur le Lightning Network. Ce graphe peut également indiquer quels canaux sont les plus sollicités et/ou qui possèdent des capacités considérables.

![markets](assets/fr/13.webp)


## Outils

Amboss met en avant un certain nombre d'outils qui vous permettent d'optimiser vos recherches et vos actions.

### Le décodeur Lightning Network

Cet outil se charge principalement de vous donner les détails de la structure d'une facture Lightning, d'une adresse Lightning ou d'une URL Lightning.

Sur la page d'accueil, dans la section **Outils**, soumettez votre adresse Lightning par exemple.

![decoder](assets/fr/14.webp)

À partir de ce décodeur, vous obtenez les informations telles que :
-  la clé publique du nœud associée à votre adresse Lightning;
- Le temps d'expiration d'une facture issue de votre adresse;
- Le minimum et maximum que vous pouvez envoyer;
- Le nœud Nostr associé à votre adresse dans le cas où Nostr est activé sur ce nœud.

![decode](assets/fr/15.webp)

### Magma IA

Découvrez le tout dernier outil présenté par Amboss pour gérer efficacement vos connexions aux nœuds du Lightning Network. Magma AI s’appuie sur une intelligence artificielle spécialement conçue pour se focaliser sur un problème important : faire une bonne sélection de nœuds auxquels se connecter.

![magma](assets/fr/16.webp)

### Calculateur de Satoshi

Prenez connaissance du prix actuel du bitcoin dans votre devise locale (EUR / USD). Sur la page d'accueil, utilisez le calculateur de satoshis pour connaitre le prix sur le marché.

![calculator](assets/fr/17.webp)


Vous avez désormais fait un tour complet des fonctionnalités et outils d'analyses de la plateforme. Nous vous proposons de retrouver, ci-dessous, notre article sur l'explorateur Bitcoin **Mempool.space**.

https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f
