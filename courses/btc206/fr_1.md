---
name: Les Inscriptions sur Bitcoin au travers d'Ordinals
goal: Comprendre le fonctionnement technique et effectif d'Ordinals
objectives:
  - Définir les notions théoriques d'Ordinals
  - Savoir comment les données sont inscrites sur Bitcoin 
  - Utiliser des outils pour explorer les inscriptions.
  - Comprendre les projets qui utilisent Ordinals
---


# 0/ Précautions

⚠️ **ATTENTION**  
La pérennité d'Ordinals n'est pas garantie. Ce protocole pourrait devenir obsolète à long terme.  
Ceci reste une expérimentation en version bêta (au 01/09/24), précédemment en phase alpha jusqu'au 25/06/24, et peut donc subir des modifications majeures.

La version actuelle est : `ord 0.19.1`.

Étant donné la nouveauté du protocole, il n'existe pas encore de spécialistes formés sur ce sujet. J'ai découvert Ordinals en février 2023 et je suis simplement un explorateur de ce protocole.

Les informations partagées ici sont une synthèse de mes connaissances et expériences, susceptibles d'évoluer. Comme pour Bitcoin, il est crucial de rester informé des évolutions de ce protocole.

## 1. Préambule

J'ai choisi une approche différente de celle généralement adoptée pour expliquer les protocoles, comme le montre [What is Ordinals and runes protocol?](https://youtu.be/g1jsHW-MX7A?si=5G3yOW0nVDIWR-38).

J'ai décidé de privilégier l'explication de l'enveloppe, qui constitue selon moi le cœur de cette innovation, avant d'aborder les satoshis et la *ordinal theory*.  
Les projets que nous discutons et présentons visent à sensibiliser et expliquer l'évolution en cours. Ce module est une introduction générale à Ordinals. Des formations plus approfondies seront proposées, et l'histoire de ces développements pourrait être détaillée dans des pages spécialisées.

**Définition (Protocole, messages protocolaires)** : Un protocole est un ensemble de règles suivi par un réseau (informatique ou humain) pour fournir un service. Les **messages protocolaires** sont les communications qui suivent ces règles établies.

*Exemples* :
- **Bitcoin** est un protocole monétaire informatique, ses messages sont des transactions.
- **HTTP** (*HyperText Transfer Protocol*) est un protocole pour échanger des pages web ou des fichiers via le protocole Internet, ses messages sont appelés [requêtes](https://www.ionos.fr/digitalguide/hebergement/aspects-techniques/requete-http/).
- Le processus de vote des lois est un protocole humain, ses messages sont les échanges durant le processus décisionnel et la communication de la validation officielle.

# I/ Introduction

Ordinals a été proposé par Casey Rodarmor[^1].

<!--Transcript depuis [Casey Rodarmor - From Ordinals to Runes: Meet Bitcoin’s Most Controversial Dev](https://www.youtube.com/watch?v=sqfCarDdXPM) :-->

En 2019, Casey découvre [Art Blocks | Generative digital art](https://www.artblocks.io/), une plateforme qui publie et promeut l'art génératif. Fasciné par cette algorithmisation de l'art, il souhaite y contribuer. En explorant les NFTs, il identifie des lacunes majeures, notamment la nécessité de déployer un contrat pour inscrire une URL menant à un lien IPFS stockant un JPEG. Convaincu que les données devraient être inscrites *on-chain*, et en tant que maximaliste de Bitcoin[^2], il développe un outil permettant d'inscrire **concrètement** l'image sur Bitcoin.

C'est ainsi que **Ordinals** est né.

Le protocole Ordinals a été utilisé pour la première fois le 14 décembre 2022 [Inscription #0](https://ordiscan.com/inscription/0).
Fondamentalement, Ordinals facilite l'inscription et la récupération de données sur Bitcoin.

Dans *L'élégance de Bitcoin* (Les contrats autonomes, l'inscription de données arbitraires et métaprotocoles pp.332-340), **Ludovic Lars** découvre des trésors cachés dans Bitcoin comme l'hommage à Len Sassaman en art ASCII ![hommage_len](./assets/hommage_len.jpg) [source image](https://hellotoken.io/dordinals/) et bien d'autres[^3].

Bien que l'inscription de données sur Bitcoin ne soit pas nouvelle, leur récupération reste compliquée, souvent car ces éléments ne sont pas indexés nativement[^4].

Ordinals répond à cette problématique. Il utilise des **enveloppes**, des **index** (ou indexeurs[^5]), et les **satoshis** (les unités de Bitcoin), pour tracer la propriété.  
Nous allons donc explorer le fonctionnement de ce protocole, son utilisation pratique, et présenter quelques projets clés de l'écosystème Ordinals.

Avant de continuer, il est pertinent de se demander : Ordinals est-il unique ?

## Ordinals est-il unique ?

D'autres protocoles à enveloppe existent, tant sur Bitcoin, comme Atomicals, que sur d'autres blockchains, telles que Dogecoin (avec Doginals).

### Atomicals

Proposé fin 2023, Atomicals est accessible via une interface en ligne de commande construite en JavaScript : [atomicals-js](https://github.com/atomicals/atomicals-js). Comme Ordinals, ce protocole nécessite une indexation, assurée par un indexer spécifique basé sur ElectrumX : [Electrumx Atomicals Indexer Server](https://github.com/atomicals/atomicals-electrumx).

Atomicals gère ses messages de manière plus compacte qu'Ordinals, utilisant une enveloppe plus simple. Plutôt que d'écrire directement les données en hexadécimal sur Bitcoin, il les transcrit d'abord en CBOR (*Concise Binary Object Representation*) puis en hexadécimal. Atomicals permet également la création native de : tokens, de NFTs et de noms de domaine, appelés *realms*.

Une avancée majeure attendue pour Atomicals est l'introduction de l'Atomicals Virtual Machine (AVM), qui offrirait la possibilité de déployer des contrats autonomes sur Bitcoin (pas encore disponible actuellement).

Bien que ce protocole offre de nombreuses possibilités sur Bitcoin, il souffre d'un manque de notoriété et d'une communauté réduite comparée à celle d'Ordinals. Des cours futurs aborderont plus en détail Atomicals. Pour plus d'informations, vous pouvez consulter [la documentation réalisée par la communauté](https://atomicals-community.github.io/atomicals-guide/).

### Doginals

Doginals est une adaptation du protocole Ordinals pour la blockchain Dogecoin[^9], utilisant la même enveloppe. Cependant, les développements sur Doginals ont souvent quelques mois de retard par rapport à Ordinals. Utiliser Ordinals sur Dogecoin présente des avantages, notamment des coûts d'inscription nettement plus bas et une rapidité accrue des transactions.

La culture autour de Doginals est légèrement différente, plus orientée vers celle de Dogecoin. Bien que les volumes d'échange soient minimes par rapport à ceux d'Ordinals, il existe tout de même une certaine activité. Doginals est limité par la qualité de ses indexers et par le développement encore embryonnaire de ses outils d'interaction.

L'intégration prochaine de Doginals dans [mydoge wallet](https://www.mydoge.com/) pourrait faciliter son utilisation et sa diffusion. Les principaux sites pour l'achat et la vente d'inscriptions Doginals sont [doggy.market](https://doggy.market) et [drc-20.org](https://drc-20.org/)[^6].

Bien que les protocoles d'inscription comme Atomicals offrent une approche assez différente de celle d'Ordinals, comprendre Ordinals est bénéfique pour saisir les évolutions futures de ces technologies.




[^1]: ([Casey (@rodarmor) | Twitter](https://twitter.com/rodarmor/), [R O D A R M O R](https://rodarmor.com/), [casey (Casey Rodarmor) | Github](https://github.com/casey/))

[^2]: Bitcoin maximaliste se dit des personnes mettant en avant le fait que Seul Bitcoin a une véritable valeur monétaire. Les autres cryptos sont en général désignées par *Shitcoin* de la part des maximalistes. Il existe plusieurs courant du maximalisme allant du minimalisme au toxic maximalisme. Les détails dépassent largement le cadre de cet introduction à Ordinals.  

[^3]: Pour un peu d'histoire cypherpunk : [Len Sassaman and Satoshi: a Cypherpunk history | Medium](https://evanhatch.medium.com/len-sassaman-and-satoshi-e483c85c2b10).

[^4]: En effet, il est possible de retrouver ces données sur Internet par exemple mais très difficile on-chain (depuis Bitcoin).

[^5]: En français on prononce indexeUr et non indexé, comme explorer (exploreUr et non exploré).

[^6]: Standard basé sur brc-20 pour Doginals. Nous détaillerons plus tard ce qu'est le standard brc-20.

[^7]: On appelle <u>réseau Bitcoin</u>, l'ensemble des machines exécutant le protocole Bitcoin. On trouvera un détail des clients utilisés pour accéder au réseau Bitcoin sur [Coin Dance | Bitcoin Nodes Summary](https://coin.dance/nodes/share).

[^8]: Attention, ces outils peuvent être obsolètes ou ne pas être sécurisés. Il est important de bien se renseigner avant d'utiliser un outil et de ne pas mettre tout son argent dans un seul outil !

[^9]: Techniquement il y a des différences assez importantes dû au code de Dogecoin qui n'est pas à jour par rapport à Bitcoin. Taproot n'est pas implémenté. 

[^10]: [RFC 2045 | Format of Internet Message Bodies](https://datatracker.ietf.org/doc/html/rfc2045), [RFC 2046 | Media Types](https://datatracker.ietf.org/doc/html/rfc2046).

[^11]: Les chiffres historique à ce sujet manque mais vous pouvez chercher sur [OpenOrdex](https://openordex.org/collection?slug=bitcoin-shrooms) si cela vous intéresse. 

[^12]: 

[^13]: Plus gros airdrop Bitcoin jamais réalisé ayant occasioné le minage du bloc: [Block 832849](https://mempool.space/block/00000000000000000000e37d10aa5a5ece8dba4a20f011280ae3d1880414ff7e). Un *airdrop* est un envoi gratuit d'inscription(s) ou de jeton(s). 

[^14]: En ce moment, mempool.space propose un service d'accéleration de transaction basé sur ce principe d'accord (off-chain, pris entre le mineur et l'utilisateur par l'intermédiaire de mempool). Est-ce que ces accords successifs avec TaprootWizards et Runestone ont joués pour quelque chose ?


[^15]: Pour un exemple de protocole *stateless* on peut penser à Bitcoin qui ne stocke que les UTXO et non pas les états des adresses (nativement) en opposition à Ethereum qui stocke les états de chaque adresses au cours du temps. Ethereum est un exemple de protocole *stateful*. 
