---
name: Ashigaru - Whirlpool Coinjoin
description: Comment faire des coinjoins sur l'application Ashigaru ?
---

![cover](assets/cover.webp)

"*a bitcoin wallet for the streets*"

Dans ce tutoriel, vous allez apprendre ce qu'est un coinjoin et comment en réaliser avec l'application Ashigaru Terminal et l'implémentation Whirlpool, un protocole de coinjoin hérité de Samourai Wallet.

## Le fonctionnement des coinjoins Whirlpool

Dans ce tutoriel, je ne reviendrai pas sur la notion de coinjoin, son utilité ou le fonctionnement théorique de Whirlpool, puisque ces sujets sont déjà expliqués en détail dans la partie 5 de la formation BTC 204 sur Plan ₿ Academy. Si vous ne maîtrisez pas encore le fonctionnement de Whirlpool ou le principe d’un coinjoin, je vous recommande vivement de consulter cette partie 5 avant de poursuivre :

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Voici toutefois quelques informations rapides qui pourront vous être utiles.

Les portefeuilles compatibles avec Whirlpool utilisent 4 comptes distincts pour répondre aux besoins du processus de coinjoin :
- Le compte **Deposit**, identifié par l’index `0'` ;
- Le compte **Bad Bank** (ou *doxxic change*), identifié par l’index `2 147 483 644'` ;
- Le compte **Premix**, identifié par l’index `2 147 483 645'` ;
- Le compte **Postmix**, identifié par l’index `2 147 483 646'`.

Sur Ashigaru, en novembre 2025, deux dénominations de pools sont disponibles (cette liste évoluera probablement dans les prochains mois: pensez donc à vérifier les valeurs au moment de votre lecture) :
- `0.25 BTC`, avec des frais d’entrée de `0.0125 BTC` ;
- `0.025 BTC`, avec des frais d’entrée de `0.00125 BTC`.

Chaque cycle de mixage peut impliquer entre 5 et 10 UTXOs en input et en output.

![Image](assets/fr/01.webp)

## Les logiciels prérequis

Pour effectuer des coinjoins avec Whirlpool, vous aurez besoin de trois logiciels distincts :  

- **Ashigaru Terminal**, qui vous permettra de gérer vos coinjoins directement depuis votre ordinateur ;

https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

- **Ashigaru Wallet**, l'application sur votre smartphone avec laquelle vous pourrez dépenser vos bitcoins en *postmix* depuis n’importe où ;

https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

- **Dojo**, une implémentation de nœud Bitcoin vous garantissant une connexion souveraine au réseau, sans dépendance envers un serveur tiers.

https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Installez chacun de ces outils en suivant leurs tutoriels respectifs, puis vous pourrez commencer à effectuer vos premiers coinjoins.

## Recevoir des bitcoins

Après la création de votre portefeuille, vous commencerez avec un seul compte, identifié par l’index `0'`. Il s’agit du compte `Deposit`. C’est sur ce compte que vous devrez envoyer les bitcoins destinés aux coinjoins. Vous pouvez les recevoir soit via l’application Ashigaru (voir la partie 5 du tutoriel dédié), soit via Ashigaru Terminal (également détaillé dans la partie 5 du tutoriel dédié).

Une fois que votre compte de dépôt contient au moins le montant nécessaire pour participer à la plus petite pool (en y ajoutant les frais de service et le minimum requis pour couvrir les frais de minage), vous serez prêt à initier vos premiers coinjoins.

![Image](assets/fr/02.webp)

## Faire la Tx0

Une fois que les fonds sont bien arrivés sur votre compte de dépôt et que la transaction est confirmée, vous pouvez lancer le processus de coinjoin. Pour cela, sur Ashigaru Terminal, ouvrez le menu `Wallets`, puis sélectionnez votre portefeuille. Si celui-ci est verrouillé, le logiciel vous demandera votre mot de passe et votre passphrase.

![Image](assets/fr/03.webp)

Sélectionnez ensuite le compte `Deposit`.

![Image](assets/fr/04.webp)

Rendez-vous dans le menu `UTXOs`.

![Image](assets/fr/05.webp)

Vous verrez ici la liste de tous les UTXOs présents sur votre compte de dépôt. Sélectionnez ceux que vous souhaitez envoyer dans les cycles de coinjoins.

Pour une meilleure confidentialité et afin d’éviter la *Common Input Ownership Heuristic (CIOH)*, il est recommandé d’utiliser un seul UTXO par entrée dans Whirlpool (vous trouverez une explication détaillée de ce principe dans la formation BTC 204).

Appuyez sur la touche `ENTER` de votre clavier pour sélectionner un UTXO : une astérisque `(*)` apparaîtra à côté pour indiquer qu’il est bien sélectionné.

![Image](assets/fr/06.webp)

Cliquez ensuite sur le bouton `Mix Selected`.

![Image](assets/fr/07.webp)

Si vous possédez un UTXO suffisamment important pour participer à l’une ou l’autre des deux pools disponibles, vous pourrez choisir la pool de destination à l’aide des flèches. Sur cette page, vous verrez les détails de votre Tx0 :
- le nombre d’UTXOs qui vont entrer dans la pool ;
- les différents frais appliqués (frais de service et frais de minage) ;
- le montant du *doxxic change*.

Vérifiez attentivement les informations, puis cliquez sur `Broadcast` pour diffuser la Tx0.

![Image](assets/fr/08.webp)

Ashigaru vous affichera ensuite le TXID de votre Tx0, ce qui confirme que la transaction a bien été diffusée sur le réseau.

![Image](assets/fr/09.webp)

## Faire les coinjoins

Une fois la Tx0 diffusée, retournez sur la page d’accueil de votre compte de dépôt, puis cliquez sur `Accounts` et sélectionnez le compte `Premix`.

![Image](assets/fr/10.webp)

Dans le menu `UTXOs`, vous verrez les différentes pièces égalisées, prêtes à entrer dans les cycles de coinjoin. Dès que la Tx0 sera confirmée, Ashigaru Terminal pourra initier automatiquement leur premier cycle de mixage.

![Image](assets/fr/11.webp)

Une fois la Tx0 confirmée, la première transaction de coinjoin sera créée et diffusée automatiquement par Ashigaru Terminal. En vous rendant dans `Accounts > Postmix > UTXOs`, vous pourrez visualiser vos UTXOs égalisés, en attente de confirmation de leur premier cycle.

![Image](assets/fr/12.webp)

Vous pouvez désormais laisser Ashigaru Terminal tourner en tâche de fond : il continuera à mixer et remixer vos pièces de manière automatique.

## Terminer les coinjoins

Vous pouvez désormais laisser vos pièces se remixer automatiquement. Le modèle de Whirlpool fait qu’aucun frais supplémentaire n’est appliqué lors des remix : ni frais de service, ni frais de minage. Laisser vos pièces participer à davantage de cycles de mixage ne peut donc être que bénéfique pour votre confidentialité.

Pour mieux comprendre ce mécanisme et savoir combien de cycles il est pertinent d’attendre, je vous recommande la lecture de cet article :

https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Pour consulter le nombre de remix réalisés par chacune de vos pièces, ouvrez le menu `UTXOs` du compte `Postmix`.

![Image](assets/fr/13.webp)

Pour dépenser vos pièces mixées, rendez-vous sur l’application Ashigaru, qui utilise le même portefeuille que votre logiciel Ashigaru Terminal. Le portefeuille affiché à l’ouverture correspond à votre compte `Deposit`. Pour accéder au compte `Postmix`, qui contient vos UTXOs mixés, cliquez sur le symbole de Whirlpool en haut à droite.

![Image](assets/fr/14.webp)

Dans ce compte, vous verrez toutes vos pièces en cours de mixage. Pour les dépenser, appuyez sur le symbole `+` en bas à droite de l’écran, puis sélectionnez `Send`.

![Image](assets/fr/15.webp)

Renseignez les détails de votre transaction : l’adresse du destinataire, le montant à envoyer, et, si vous le souhaitez, choisissez une structure de transaction spécifique pour renforcer encore davantage votre confidentialité (voir les tutoriels correspondants).

![Image](assets/fr/16.webp)

Vérifiez attentivement les informations de la transaction, puis faites glisser la flèche en bas de l’écran pour confirmer l’envoi.

![Image](assets/fr/17.webp)

Votre transaction a bien été signée et diffusée sur le réseau Bitcoin.

![Image](assets/fr/18.webp)

## Dépenser le Doxxic Change

Souvenez-vous : le modèle de Whirlpool repose sur une étape d’égalisation de vos pièces lors de la Tx0, avant leur entrée dans les pools. C’est ce mécanisme qui permet de briser le traçage des UTXOs. Ce modèle est, selon moi, le plus efficace en matière de coinjoin, mais il présente un inconvénient : il génère un *change* qui ne passe pas dans le processus de coinjoin.

Ce change correspond à un UTXO créé pour chaque Tx0. Il est isolé dans un compte spécifique nommé `Doxxic Change` ou `Bad Bank`, selon les logiciels, afin d’éviter de l'utiliser avec vos autres UTXOs. Ce point est très important, car ces UTXOs n’ont pas été mixés : leurs liens de traçabilité demeurent intacts, et ils peuvent compromettre votre confidentialité en établissant une connexion entre vous et votre activité de coinjoin. Il faut donc les manipuler avec précaution et **ne jamais les utiliser avec d’autres UTXOs**, qu’ils soient mixés ou non. Combiner un UTXO toxique avec un UTXO mixé anéantirait tout le gain de confidentialité acquis lors des coinjoins.

Pour l’instant, Ashigaru ne propose pas d’accès direct à ce compte `Doxxic Change` (en tout cas, je ne l'ai pas trouvé). Cette fonctionnalité sera probablement ajoutée dans une future mise à jour. En attendant, la seule méthode pour récupérer ces fonds consiste à importer votre seed dans Sparrow Wallet. Ce dernier détectera normalement automatiquement qu’il s’agit d’un portefeuille utilisé avec Whirlpool et vous donnera accès aux quatre comptes, dont celui du `Doxxic Change`. Vous pourrez alors dépenser ces UTXOs comme des bitcoins classiques depuis Sparrow.

Voici plusieurs stratégies possibles pour gérer vos UTXOs de change issus des coinjoins sans compromettre votre confidentialité :

- **Les mixer dans des pools plus petites :** Si votre UTXO toxique est suffisamment important pour rejoindre une pool de plus petite taille, c’est généralement la meilleure option. Attention toutefois à ne jamais fusionner plusieurs UTXOs toxiques pour y parvenir, car cela créerait un lien entre vos différentes entrées dans Whirlpool.

- **Les marquer comme non dépensables :** Une autre approche prudente consiste simplement à les conserver tels quels dans leur compte séparé et à ne pas y toucher. Vous éviterez ainsi de les dépenser accidentellement. Si la valeur du bitcoin augmente, de nouvelles pools adaptées à leur taille pourraient être ouvertes.

- **Faire des donations :** Vous pouvez choisir de transformer ces UTXOs toxiques en dons aux développeurs Bitcoin, aux projets open-source ou à des associations acceptant le BTC. Cela vous permet de vous en débarrasser utilement tout en soutenant l’écosystème.

- **Acheter des cartes-cadeaux ou cartes Visa prépayées :** Des plateformes comme [Bitrefill](https://www.bitrefill.com/) permettent d’échanger vos bitcoins contre des cartes cadeaux ou des cartes Visa rechargeables utilisables dans le commerce. Cela peut être une manière simple et discrète de dépenser vos UTXOs toxiques.

- **Les échanger contre du Monero :** Samourai Wallet proposait autrefois un service de swap atomique BTC/XMR, aujourd’hui disparu. Si un service similaire existe (je n'en connais pas personnellement), il constitue une excellente solution pour isoler ces UTXOs, les convertir en Monero, puis éventuellement les renvoyer sur Bitcoin. Cette méthode était cependant coûteuse et dépendante de la liquidité disponible.

- **Les transférer sur le Lightning Network :** Transférer ces UTXOs sur le Lightning Network pour bénéficier de frais de transaction réduits est une option qui peut être intéressante. Cependant, cette méthode peut révéler certaines informations selon votre utilisation de Lightning et doit donc être pratiquée avec prudence.

## Comment connaître la qualité de nos cycles de coinjoin ?

Pour qu’un coinjoin soit véritablement efficace, il doit présenter une forte homogénéité entre les montants des entrées et des sorties. Cette uniformité augmente le nombre d’interprétations possibles pour un observateur externe, ce qui renforce ainsi l’incertitude sur la transaction. Pour mesurer cette incertitude, on utilise le concept d’entropie appliqué à la transaction. Le modèle de Whirlpool est reconnu comme l’un des plus performants à ce niveau, car il garantit une excellente homogénéité entre les participants. Pour approfondir ce principe, je vous recommande de consulter le dernier chapitre de la partie 5 de la formation BTC 204.

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

La performance de plusieurs cycles de coinjoins se mesure quant à elle à travers la taille des ensembles dans lesquels une pièce est dissimulée. Ces ensembles définissent ce que l’on appelle les *anonsets*. Il en existe deux types : le premier évalue la confidentialité face à une analyse rétrospective (du présent vers le passé), et le second mesure la résistance à une analyse prospective (du passé vers le présent). Pour une explication complète de ces deux indicateurs, je vous invite à lire le tutoriel suivant (ou bien, encore une fois, la formation BTC 204) :

https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Comment gérer le postmix ?

Après avoir effectué plusieurs cycles de coinjoins, la meilleure stratégie consiste à conserver vos UTXOs dans le compte `Postmix`, en les laissant se remixer indéfiniment jusqu’à ce que vous ayez réellement besoin de les dépenser.

Certains utilisateurs préfèrent transférer leurs bitcoins mixés vers un portefeuille sécurisé par un hardware wallet. Cette option est possible, mais elle demande une certaine rigueur par la suite afin de ne pas compromettre la confidentialité acquise grâce aux coinjoins.

La fusion d’UTXOs est l’erreur la plus fréquente. Il est important de ne jamais combiner, dans une même transaction, des UTXOs mixés avec des UTXOs non mixés, sous peine de déclencher la *Common Input Ownership Heuristic (CIOH)*. Cela implique une gestion rigoureuse de vos UTXOs, notamment à travers un étiquetage clair et précis. D’une manière générale, la fusion d’UTXOs est une mauvaise pratique qui entraîne souvent une perte de confidentialité lorsqu’elle est mal maîtrisée.

https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Soyez également prudent avec la consolidation d’UTXOs mixés entre eux. Des consolidations limitées peuvent être envisagées si les UTXOs disposent d’anonsets importants, mais elles réduisent inévitablement votre niveau de confidentialité. Évitez les consolidations massives ou précipitées, réalisées avant un nombre suffisant de remixages, car elles pourraient établir des liens déductibles entre vos pièces avant et après mixage. En cas de doute, il est préférable de ne pas consolider vos UTXOs postmix et de les transférer un à un vers votre hardware wallet, en générant chaque fois une nouvelle adresse de réception vierge. Pensez également à bien étiqueter chaque UTXO transféré.

Il est fortement déconseillé de déplacer vos UTXOs postmix vers des portefeuilles utilisant des scripts minoritaires. Par exemple, si vous avez participé à Whirlpool depuis un portefeuille multisig en `P2WSH`, vous serez peu nombreux à partager ce type de script. En renvoyant vos UTXOs postmix vers ce même type de script, vous réduisez considérablement votre anonymat. Au-delà du type de script, d’autres empreintes de portefeuille spécifiques peuvent compromettre votre confidentialité, c'est pourquoi le mieux reste de les dépenser depuis l'application Ashigaru.

Enfin, comme pour toute transaction Bitcoin, ne réutilisez jamais une adresse de réception. Chaque paiement doit être envoyé vers une nouvelle adresse unique et vierge.

La méthode la plus simple et la plus sûre reste donc de laisser vos UTXOs mixés au repos dans leur compte `Postmix`, de les laisser se remixer naturellement, et de ne les dépenser qu’en cas de besoin depuis Ashigaru.

Les portefeuilles Ashigaru et Sparrow intègrent des protections supplémentaires contre les erreurs les plus courantes liées à l’analyse de chaîne, ce qui vous aidera à préserver la confidentialité de vos transactions.
