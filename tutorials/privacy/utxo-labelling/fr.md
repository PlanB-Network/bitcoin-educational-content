---
name: Labelling UTXO
description: Comment bien étiqueter ses UTXO ?
---
![cover](assets/cover.jpeg)





## Qu'est-ce que le labelling d'UTXO ?
Le "labelling" est une technique consistant à associer une annotation ou une étiquette à un UTXO spécifique au sein d'un portefeuille Bitcoin. Ces annotations sont stockées localement par le logiciel de portefeuille et ne sont jamais transmises sur le réseau Bitcoin. Le labelling est ainsi un outil de gestion personnel.

Par exemple, si je reçois un UTXO d'une transaction P2P via Bisq avec Charles, je pourrais lui attribuer l'étiquette `No-KYC Bisq Charles`.

Le labelling permet de se souvenir de l'origine ou de la destination envisagée de l'UTXO, ce qui simplifie la gestion des fonds et l'optimisation de la confidentialité de l'utilisateur. L'étiquetage devient encore plus pertinent lorsqu'il est combiné avec la fonctionnalité de "coin control". Le coin control est une option disponible dans les bons portefeuilles Bitcoin, qui offre à l'utilisateur la possibilité de choisir manuellement quels UTXO spécifiques seront utilisés comme entrées lors de la création d'une transaction.

L'utilisation d'un portefeuille avec du coin control, couplé à l'étiquetage des UTXO, permet aux utilisateurs de distinguer et de sélectionner avec précision les UTXO pour leurs transactions, évitant ainsi de combiner des UTXO provenant de sources différentes. Cette pratique réduit les risques liés à l'heuristique d'analyse de chaîne CIOH (_Common Input Ownership Heuristic_), qui suggère une propriété commune des entrées d'une transaction, ce qui peut compromettre la confidentialité de l'utilisateur.

Reprenons l'exemple de mon UTXO no-KYC issu de Bisq ; je souhaite éviter de le combiner avec un UTXO provenant, disons, d'une plateforme d'échange réglementée connaissant mon identité. En apposant une étiquette distincte sur mon UTXO no-KYC et sur mon UTXO KYC, je pourrai aisément identifier quel UTXO consommer en input pour satisfaire une dépense, en me servant de la fonctionnalité de coin control.

## Comment bien étiqueter ses UTXO ?
Il n'y a pas de méthode universelle pour l'étiquetage des UTXO qui puisse convenir à tous. C'est à vous de définir un système d'étiquetage pour que vous puissiez facilement vous y retrouver sur votre portefeuille. 

Un critère primordial dans l'étiquetage est la source de l'UTXO. Vous devriez simplement indiquer la manière dont cette pièce est parvenue dans votre portefeuille. Est-elle issue d'une plateforme d'échange ? D'un règlement de facture par un client ? D'un échange pair-à-pair ? Ou représente-t-elle le change d'une dépense ? Ainsi, vous pourriez spécifier :
- `Retrait Exchange.com` ;
- `Paiement Client X` ;
- `Achat P2P Charles` ;
- `Change achat canapé`.

Pour affiner votre gestion des UTXO et respecter vos stratégies de ségrégation de fonds au sein de votre portefeuille, vous pourriez enrichir vos étiquetages d'un indicateur supplémentaire qui reflète ces choix. Si votre portefeuille contient deux catégories d'UTXO que vous tenez à ne pas mélanger, vous pourriez intégrer un marqueur distinctif dans vos étiquettes pour distinguer clairement ces groupes. Ces marqueurs de séparation dépendront de vos propres critères, tels que la distinction entre UTXO KYC (connaissant votre identité) et no-KYC (anonymes), ou encore entre fonds professionnels et personnels. En reprenant les exemples d'étiquettes mentionnés précédemment, cela pourrait se traduire par :
- `KYC - Retrait Exchange.com` ;
- `KYC - Paiement Client X` ;
- `NO KYC - Achat P2P Charles` ;
- `NO KYC - Change achat canapé`.

Dans tous les cas, gardez à l'esprit qu'un bon étiquetage est un étiquetage que vous pourrez comprendre lorsque vous en aurez besoin. Si votre portefeuille Bitcoin est principalement destiné à l'épargne, il se peut que les étiquettes ne vous soient utiles que dans plusieurs décennies. Assurez-vous donc qu'elles soient claires, précises et exhaustives.

Il est également conseillé de perpétuer l'étiquetage d'une pièce au fil des transactions. Par exemple, lors d'une consolidation d'UTXO no-KYC, assurez-vous de marquer l'UTXO résultant non pas seulement comme `consolidation`, mais spécifiquement comme `consolidation no-KYC` pour conserver une trace claire de sa provenance.

Quant à l'ajout d'une date sur les étiquettes, ce n'est pas une nécessité. La plupart des portefeuilles logiciels affichent déjà la date de transaction, et il est toujours possible de retrouver cette information sur un explorateur de blocs grâce au TXID de la transaction.

Enfin, il n'est pas obligatoire de mettre une date sur une étiquette. La plupart des logiciels de portefeuilles affichent déjà la date de transaction, et il est toujours possible de retrouver cette information sur un explorateur de blocs grâce au TXID de la transaction.

## Tutoriel : étiqueter sur Green Wallet






## Tutoriel : étiqueter sur Samourai Wallet






## Tutoriel : étiqueter sur Sparrow Wallet








## Tutoriel : étiqueter sur le wallet Bitcoin Core









## Tutoriel : étiqueter sur Blue Wallet








## Tutoriel : étiqueter sur Electrum











## Tutoriel : étiqueter sur Specter Wallet