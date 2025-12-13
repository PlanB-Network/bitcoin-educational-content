---
name: Bitfeed
description: Explorez la chaine principale du protocole Bitcoin.
---

![cover](assets/cover.webp)

Bitfeed est une plateforme de visualisation de la couche principale (onchain) du protocole Bitcoin. Elle a été initiée par un des contributeurs du projet Mempool.space et se démarque principalement par son aspect minimaliste et son utilisation simple.

https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Dans ce tutoriel, nous partons à la découverte de cet outil qui vous permet d'explorer l'ensemble des transactions et blocs du réseau.

## Débuter avec Bitfeed

Bitfeed est une plateforme qui se focalise sur trois principaux points :

- **La consultation de la chaîne de blocs**,
- **La recherche de transactions**,
- **La visualisation du mempool**.

### La consultation de la chaîne de blocs

Sur la page d'accueil de Bitfeed, vous retrouverez essentiellement :

- La barre de recherche : Cette section est le point d'entrée des interrogations sur la chaîne de blocs. Vous pouvez y rechercher un bloc spécifique via le numéro ou le hash dudit bloc. Vous avez également la possibilité de rechercher des transactions spécifiques et des adresses Bitcoin afin de vérifier certaines informations sur les transactions sur le réseau.

![searchBar](assets/fr/01.webp)

Dans l’angle supérieur gauche, vous pouvez consulter le prix actuel du bitcoin, estimé en dollars américains (USD).

![price](assets/fr/02.webp)

Sur la barre latérale de droite se trouve le menu de la plateforme. À partir de ce menu vous pouvez personnaliser l'interface de la plateforme selon votre convenance, ajouter ou retirer des éléments et personnaliser les filtres de visualisation. Par exemple, visualiser la taille de chaque bloc par valeur ou par poids en octets virtuels (vBytes).

![menu](assets/fr/03.webp)

Au centre de la page se trouve le dernier bloc miné avec la visualisation de l'ensemble des transactions incluses dans ce bloc. Cette section nous renseigne sur l'horodatage, la totalité des bitcoins impliqués dans ce bloc, la taille en octets du bloc, le nombre de transactions et la moyenne du ratio de frais de transaction par octet virtuel dans le bloc.

![block](assets/fr/04.webp)

Vous pouvez remonter l'historique de la chaîne en cherchant un bloc spécifique dans la barre de recherche et vous pourrez le visualiser selon vos critères.

Prenons un exemple, nous souhaitons visualiser les transactions du bloc `879488`.

![bloc](assets/fr/05.webp)

La première transaction de ce bloc représente la transaction **coinbase** qui permet au mineur de ce bloc de gagner la récompense de minage, laquelle n’est dépensable qu’après 100 blocs minés, composée des frais des transactions incluses et de la subvention de bloc. Cette transaction est celle qui permet l'émission de nouveaux bitcoins sur le système.

![coinbase](assets/fr/06.webp)

https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f

Par défaut les transactions d'un bloc sont représentées selon deux critères :
- La taille qui peut varier entre la valeur et le poids (vBytes) ;
- La couleur qui peut varier entre l'âge et le ratio des frais de transactions par octet virtuel.

![options](assets/fr/07.webp)

Nous pouvons donc en conclure que toutes les transactions incluses dans un même bloc possèdent le même nombre de confirmations dans la chaîne de blocs. Les cubes les plus volumineux représentent quant à eux les transactions contenant le plus grand montant de bitcoins.

Cette interprétation est d'autant plus confirmée par l'option **"Infos"** du menu qui nous renseigne sur la traduction de la couleur et de la taille des transactions du bloc.

![infos](assets/fr/08.webp)

Vous pouvez également visualiser les transactions d'un bloc en fonction des octets virtuels et du ratio de frais. Cette visualisation peut différer de la précédente car la valeur de bitcoin incluse dans une transaction ne définit pas la taille de cette dernière.

![visualisation](assets/fr/09.webp)

### La consultation des transactions

Vous pouvez rechercher une transaction en utilisant son identifiant via la barre de recherche. Vous pouvez également cliquer sur un cube pour avoir les informations liées à cette transaction.

Dans notre cas, prenons la transaction occupant le plus grand espace dans le bloc `879488`.

![biggest](assets/fr/10.webp)

Vous constaterez que cette transaction possède `42 989` qui représente la différence entre le dernier bloc en cours de minage et notre bloc choisi. Ces confirmations participent au renforcement de la sécurité du réseau Bitcoin car pour modifier cette transaction de façon malicieuse, les attaquants doivent posséder la puissance de calcul équivalente pour réécrire l'entièreté de la chaîne de blocs principale.

La taille de cette transaction est de `57 088 vBytes`, principalement en raison du grand nombre d’UTXOs utilisés pour sa construction (842 entrées). Fait étonnant, le ratio de frais appliqué reste relativement faible (seulement 4 sats/vByte) comparé à la moyenne globale du bloc, qui s’élève à 5,82 sats/vByte.

La transaction occupant le plus d'espace n'est donc pas forcément la transaction avec le ratio de frais de transaction le plus élevé.

![transaction](assets/fr/11.webp)

En suivant la graduation du menu **Infos**, la transaction avec le ratio de frais de transaction le plus élevé est la plus violette. Il s'agit donc de la transaction [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) ayant un ratio de frais de transaction de `147,49 sats/vBytes`.

![mostfeerate](assets/fr/12.webp)

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Visualisation du Mempool

Le mempool est l'emplacement virtuel dans lequel les transactions Bitcoin en attente d'inclusion dans un bloc sont regroupées. Bitfeed permet la consultation du [mempool](https://planb.academy/resources/glossary/mempool) de plusieurs mineurs Bitcoin offrant un large éventail de suivi de transactions.

![mempool](assets/fr/13.webp)

Dans cette section, vous pouvez suivre l'ensemble des transactions valides et encore non confirmées sur la chaîne principale du réseau Bitcoin.

![unconfirmed](assets/fr/14.webp)

Vous avez désormais un guide d'utilisation de la plateforme Bitfeed pour analyser des blocs et des transactions afin de visualiser les informations disponibles sur la chaîne principale du réseau Bitcoin tout en profitant d'une interface minimaliste et facile à prendre en main. Si vous avez aimé ce tutoriel, nous vous recommandons de passer à l'étape supérieure : découvrir le Lightning Network via le projet Amboss.

https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017
