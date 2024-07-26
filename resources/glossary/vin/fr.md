---
term: VIN
---

Élément spécifique d'une transaction Bitcoin qui spécifie la source des fonds utilisés pour satisfaire les outputs. Chaque `vin` fait référence à un output non dépensé (UTXO) d'une transaction précédente. Une transaction peut contenir plusieurs inputs, chacun étant identifié par une combinaison du `txid` (l'identifiant de la transaction d'origine) et du `vout` (l'index de l'output dans cette transaction).

Chaque `vin` inclut les informations suivantes :
* `txid` : l'identifiant de la transaction précédente contenant l'output utilisé ici en input ;
* `vout` : l'index de l'output dans la transaction précédente ;
* `scriptSig` ou `scriptWitness` : un script de déverrouillage qui fournit les données nécessaires pour satisfaire les conditions posées par le `scriptPubKey` de la transaction précédente dont les fonds sont dépensés, généralement en fournissant une signature cryptographique ;
* `nSequence` : un champ spécifique utilisé pour indiquer la manière dont cet input est verrouillé dans le temps, ainsi que d'autres options comme RBF.


