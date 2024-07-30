---
term: P2WSH
---

P2WSH est le sigle pour *Pay to Witness Script Hash* (en français « payer au témoin du hachage du script »). C’est un modèle de script standard utilisé pour établir des conditions de dépense sur un UTXO. P2WSH a été introduit avec l'implémentation de SegWit en août 2017.

Ce script est similaire à P2SH (*Pay to Public Script Hash*), puisqu'il verrouille également des bitcoins sur la base du hachage d'un script. La différence réside dans la manière dont les signatures et les scripts sont inclus dans la transaction. Pour dépenser les bitcoins sur ce type de script, le bénéficiaire doit fournir le script d'origine, appelé `witnessScript` (équivalent du `redeemScript`), ainsi que les signatures requises. Ce mécanisme permet d'implémenter des conditions de dépense plus sophistiquées, telles que des multisigs.

Dans le cadre de P2WSH, les informations du script de signature (le `scriptWitness`, l'équivalent du `scriptSig`) sont déplacées de la structure traditionnelle de la transaction vers une section distincte appelée `Witness` (témoin). Ce déplacement est une caractéristique de la mise à jour SegWit (*Segragated Witness*) qui permet d'empêcher la malléabilité liée à la signature. Les transactions P2WSH sont généralement moins coûteuses en termes de frais par rapport aux transactions Legacy, car la partie dans le témoin coûte moins cher.

Les adresses P2WSH sont écrites en utilisant l'encodage `Bech32` avec une somme de contrôle sous forme de code BCH. Ces adresses commencent toujours par `bc1q`. P2WSH est une sortie SegWit de version 0.

