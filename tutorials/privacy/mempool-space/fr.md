---
name: Mempool
description: Explorez l'ensemble de l'écosystème Bitcoin.
---

![cover](assets/cover.webp)

Le protocole Bitcoin est un réseau pseudonyme, décentralisé et ouvert à la consultation. Les membres (nœuds), c'est-à-dire les ordinateurs ayant une instance du logiciel Bitcoin peuvent avoir, sans restriction, à l'ensemble des données publiées sur Bitcoin. Toutes fois, dans les premières années de Bitcoin, le protocole n'était pas accessible à tous comme nous pouvions le voir de nos jours.
Aux premières heures de Bitcoin, il fallait faire tourner un nœud Bitcoin afin d'accéder aux outils appropriés (bitcoin-cli) pour interroger le réseau à partir des lignes de commandes.

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Des projets se sont donc initiés, pour élargir la communauté autour de Bitcoin, le rendant plus accessible à toute personne n'ayant pas de nœud et/ou n'ayant pas des compétences techniques requises.

Dans ce tutoriel, nous découvrirons le projet **Mempool.space**, ses fonctionnalités et l'impact qu'il a eu dans l'écosystème Bitcoin.

## Qu'est-ce que Mempool.space ?

**Mempool.space** est un explorateur open source qui fournit des informations utiles sur les transactions, les frais de transactions, les blocs et les mineurs sur les différents réseaux du protocole Bitcoin. Lancé en 2020, il apporte une amélioration significative de l'expérience utilisateur au travers de graphiques représentatifs, des animations fluides et des interfaces épurées.

Pour comprendre le projet, un Mempool (Memory pool - zone de mémoire), est un espace virtuel dans lequel se trouve toutes les transactions en attente de confirmation sur le réseau Bitcoin. Un Mempool est comme une "salle d'attente" où les transactions Bitcoin patientent avant d'être confirmées. Chaque ordinateur du réseau (nœud) a sa propre salle d'attente, ce qui explique pourquoi toutes les transactions ne sont pas visibles au même moment par tout le monde.

Le principal impact de la plateforme dans l'écosystème Bitcoin est qu'elle vous permet d'accéder aux informations variées des zones de mémoire de la plupart des nœuds présents sur Bitcoin sans avoir besoin d'en faire tourner un. Mempool.space constitue un référentiel pour la visualisation et la recherche sur les réseaux du protocole Bitcoin.

L'utilisation de plus en plus répandue dans l'écosystème et le fait que Mempool.space soit open source ont permis son intégration dans de plus en plus de système d'hébergement personnel. Vous pouvez donc avoir votre propre instance de Mempool.space directement sur votre nœud personnel. Retrouvez ci-dessous, notre tutoriel sur la configuration de Mempool.space sur votre nœud Umbrel.

https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Les bases de Mempool.space

Comme écrit plus haut, [Mempool.space](https://mempool.space) est un explorateur du protocole Bitcoin qui vous permet de suivre en temps réel, à partir d'une interface graphique, vos transactions et leur propagation sur le réseau Bitcoin choisit.

Mempool.space supporte de nombreux réseaux du protocole Bitcoin.
Dans la barre de menu, vous retrouverez les réseaux suivants :
- **Mainnet** : Le réseau principal de Bitcoin où s'opère les transactions réelles en bitcoin.
- **Signet** : Un réseau de test qui utilise les signatures digitales pour la validation des blocs sans demander les ressources requises par le réseau principal.
- **Testnet 3** : Un réseau de tests et de développement sans risques financiers sur le protocole Bitcoin.
- **Testnet 4** : La nouvelle version du Testnet 3 apportant plus de stabilité et de nouvelles règles de consensus à l'environnement de test.

![reseaux](assets/fr/01.webp)

Sur la page d'accueil, vous retrouverez à gauche en vert, les possibles futurs blocs (groupe de transactions) prêts à être validés et intégrés (minés) au réseau Bitcoin. Un bloc est miné en moyenne toutes les dix minutes : gardez cette information, elle vous sera utile plus bas dans notre développement.
En violacé, du côté droit, vous retrouverez les récents blocs minés sur Bitcoin, le numéro du dernier bloc miné constitue la hauteur actuelle du réseau.

![blocs](assets/fr/02.webp)

La section **Transaction Fees**, constitue un estimateur de frais de transactions, plus les frais alloués à votre transaction sont élevés, plus votre transaction est susceptible d'être ajoutée rapidement dans le prochain bloc prêt à être miné.
Les frais de transactions représentent le coût que vous prendra un mineur pour insérer votre transaction dans un bloc candidat au minage. Il est défini par un ratio de sat/vB (satoshi/Virtual Bytes) représentant le nombre de satoshis que vous payez pour l'espace que votre transaction occupera dans le bloc candidat.

⚠️ IMPORTANT : En cas de saturation de leur Mempool, les mineurs priorisent les transactions offrant le meilleur ratio satoshi/vByte. Plus votre transaction est lourde (volumineuse), plus elle devra proposer de satoshis pour être incluse rapidement.

![fees-visualizer](assets/fr/03.webp)

Vous pouvez retrouver une visualisation de l'espace occupé par une transaction grâce à la section **Mempool Goggles**.

![mempool](assets/fr/04.webp)

Un bloc est miné environ toutes les dix minutes à cause de la difficulté de la preuve de travail que les mineurs doivent fournir pour ajouter leur bloc candidat à la chaine des blocs minés. Cette difficulté varie tous les **2016 blocs** équivalant à environ **2 semaines**. Vous pouvez donc visualiser l'évolution de cette difficulté.

![difficulty](assets/fr/05.webp)

L'ajout d'un nouveau bloc à la chaine principale donne droit, au mineur du bloc validé, à une récompense composée d'une partie fixe (divisée par deux tous les **210 000 blocs** équivalant à environ **4 années** lors des halvings) et des frais de transaction.

![halving](assets/fr/06.webp)

## Accéder aux détails de vos transactions

Dans la barre de recherche de Mempool.space, vous pouvez insérer votre adresse bitcoin ou l'identifiant de votre transaction afin d'avoir plus de détails sur votre historique.

![search](assets/fr/07.webp)

Sur la page de détails des transactions, vous retrouverez les informations générales de votre transaction :
- **Son Statut** : Confirmé lorsqu'il a été ajouté à un bloc, non confirmé lorsqu'il est en attente dans un mempool.
- **Les frais de transactions**.
- **L'heure d'arrivé estimée (ETA)** :  Le temps approximatif que prendra votre transaction à être ajouté à un bloc. Il est calculé en fonction du ratio constituant les frais associés à cette transaction.

![general-txinfo](assets/fr/08.webp)

La section **Flow** vous présente un graphique des composantes de votre transactions.

Les entrées (UTXO précédents), utilisées pour votre transaction et les sorties donnant droits, aux destinataires, d'utiliser les bitcoins de chaque sortie en présentant la signature requise pour leur dépense.

![flow](assets/fr/09.webp)

Vous obtenez plus de détails sur les adresses utilisées dans la section **Inputs & Outputs**.

![address](assets/fr/10.webp)

Découvrez les différents schémas de transactions Bitcoin pour accroître votre confidentialité.

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Accélérer vos transactions

Dans l'écosystème Bitcoin, l'aspect de la validation d'une transaction par les mineurs est intrinsèquement lié au frais de transactions associées à cette transaction. Les mineurs priorisent les transactions ayant un ratio de frais (satoshis/vBytes) plus élevés, ce qui pourrait affecter la validité de votre transaction si vous ne payez pas des frais raisonnables acceptés par les mineurs. Votre transaction se retrouverait bloquée dans le mempool en attendant un bloc acceptant son ratio de frais.

Heureusement, il existe, sur le réseau Bitcoin, deux méthodes pouvant vous permettre d'accélérer la confirmation de votre transaction.

- **RBF** - Replacement By Fee : Une méthode qui vous permet de dépenser les mêmes entrées que votre transaction ayant un faible ratio de frais, mais cette fois-ci en augmentant les frais de transaction pour accélérer la validation. Votre nouvelle transaction sera plus rapidement validée et inclus dans un bloc ce qui entraînera l'invalidation de la transaction ayant un faible frais.

Vous pourrez effectuer une action de remplacement de frais avec des portefeuilles acceptant ce mécanisme. Retrouvez par exemple notre article sur le portefeuille Blue Wallet.

https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

- **CPFP** - Child Pay For Parent : Une approche inspirée du RBF mais du coté du destinataire. Lorsque la transaction dans laquelle vous êtes destinataire est bloquée dans un mempool, vous avez la possibilité de dépenser les sorties (UTXOs) de cette transaction, malgré qu'elle ne soit pas encore confirmée, en allouant plus de frais à cette nouvelle transaction afin que la moyenne des frais - de la transaction dont vous êtes destinataire et de la transaction initiée - incite les mineurs à inclure toutes les deux transactions dans un bloc.

⚠️ La première transaction doit impérativement être incluse dans un bloc pour permettre à la seconde transaction d'être confirmée.

Si tous ces termes vous semblent un peu trop techniques, je vous recommande de [consulter notre glossaire](https://planb.network/resources/glossary), qui regroupe les définitions de tous les termes techniques en lien avec Bitcoin et son écosystème.

Outre ces méthodes, Mempool.space, grâce à ses connexions avec plus de 80% des mineurs présents sur le réseau Bitcoin, vous permet également d'accélérer n'importe laquelle de vos transactions **non confirmée**, même celles n'activant pas le RBF, en payant une contrepartie aux mineurs en échange de l'insertion de votre transaction à faible frais dans le prochain bloc prêt à être miné.

Sur la page de détail de votre transaction, cliquez sur le buton **Accelerate** puis procédez au paiement de votre contrepartie aux mineurs.

![accelerate-section](assets/fr/11.webp)
## Les mineurs

Un mineur fait référence à une personne qui gère une mine, c'est-à-dire un ordinateur engagé dans le processus de minage, qui consiste à participer à la Proof-of-Work. Le mineur regroupe les transactions en attente dans sa mempool pour former un bloc candidat. Ensuite, il recherche un hachage valide, inférieur ou égal à la cible, pour l’entête de ce bloc en modifiant les différents nonces. S’il trouve un hachage valide, il diffuse son bloc au réseau Bitcoin et empoche la récompense pécuniaire associée, composée de la subvention de bloc (création de nouveaux bitcoins ex-nihilo), et des frais de transaction.

https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Les mineurs sont comme des "validateurs" qui vérifient et regroupent les transactions dans des blocs. Pour ajouter un nouveau bloc au réseau Bitcoin, ils doivent résoudre un puzzle mathématique complexe (la Proof-of-Work). Le premier mineur qui résout le puzzle gagne une récompense en bitcoin (subvention de bloc + frais des transactions incluses dans le bloc).

La difficulté de cette preuve de travail est monitorée, vous permettant ainsi de visualiser l'évolution de la puissance de calcul requise pour les mineurs. Vous retrouverez dans les sections ci dessous :

- Une estimation des récompenses totales engrangées par les mineurs au cours de dernier ajustement de la difficulté ainsi que les estimations sur la prochaine division de moitié de la subvention de bloc intervenant toutes les 210000 blocs (04 années environ).

![rewards](assets/fr/12.webp)

Cette difficulté est ajustée toutes les 2016 blocs (deux semaines environ). Elle est proportionnellement inverse à la moyenne du temps pris par les mineurs pour miner les 2016 blocs.
Lorsque le temps moyen pris par les mineurs est inférieur à 10 minutes, la difficulté s'accroît prouvant qu'il était plus facile aux mineurs de valider des miner des blocs. Inversement, lorsque le temps moyen est supérieur à 10 minutes, la difficulté décroît.

![mining-pool](assets/fr/13.webp)

- Les groupes de mineurs : Au vue de la difficulté, un ensemble de mineurs collaborent pour participer à la recherche de la preuve de travail sur Bitcoin, c'est ce que nous appellerons un **pool**. Lorsqu'un bloc est miné par le groupe, la récompense obtenue est distribuée en fonction du pourcentage de réussite dans la recherche de solution partielle de chaque mineur, c'est-à-dire l'apport en puissance de calcul dans la recherche de la Proof-of-Work, ou en fonction de la méthode de rémunération convenue par la coopération.



![mining](assets/fr/14.webp)

## L'infrastructure du Lightning Network

Mempool ne se limite pas qu'à vous fournir des informations sur les infrastructures des réseaux de Bitcoin (chaine principale). Il intègre également des outils de visualisation et d'exploration de la surcouche Lightning de Bitcoin.

Dans la section **Eclair**, vous pouvez visualiser l'ensemble des connexions existantes entre les nœuds Lightning.

![network-stats](assets/fr/15.webp)

Cette interface vous renseigne sur :

- Les statistiques du réseau Lightning.

![distribution](assets/fr/16.webp)


⚠️ **IMPORTANT** : La capacité d'un canal de paiement désigne le montant maximum qu'un nœud peut envoyer à un autre nœud lors d'une transaction Lightning.

- La répartition des nœuds Lightning en fonction du fournisseur de service Internet (service d'hébergement) et optionnellement en fonction de la capacité des canaux de paiement.

![distribution](assets/fr/17.webp)

- L'historique de la capacité générale du réseau Lightning.
Vous trouverez également un classement de ces nœuds en fonction ou non de la capacité de leurs canaux de paiement.

![ranking](assets/fr/18.webp)

## Plus de graphiques

Mempool.space est la plateforme idéale pour apprécier l'interaction avec les réseaux du protocole Bitcoin. Les graphiques fournissent non seulement des données visuelles qui vous aide à décider quand effectuer des transactions, mais également des paramètres précis vous permettant de visualiser, en temps réel la solidité, la santé du réseau Bitcoin et des infrastructures Lightning associées.

Dans la section **Graphique**, vous pouvez visualiser des données essentielles concernant le réseau Bitcoin :
- L'évolution de la taille du mempool : Vous pouvez observer comment la taille du mempool fluctue, ce qui peut vous indiquer des périodes de forte activité ou de calme sur le réseau.

![graphs](assets/fr/19.webp)


- L'évolution des transactions et frais de transaction sur le réseau choisie :  En suivant les variations des transactions par seconde, vous pouvez anticiper les périodes de congestion ou de faible activité afin d'optimiser les frais de vos transactions. Ce graphique vous offre une perspective sur la capacité du réseau à gérer le volume de transactions.

![graphs](assets/fr/20.webp)

Vous voilà à la fin de votre parcours sur Mempool.space, devenez dès maintenant votre propre explorateur et traquez vos transactions en temps réel. Nous vous proposons de retrouver, ci-dessous, notre article sur l'explorateur Bitcoin **Public Pool**.

https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1
