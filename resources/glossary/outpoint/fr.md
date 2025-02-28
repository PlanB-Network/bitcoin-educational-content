---
term: OUTPOINT
---

Référence unique à une sortie de transaction non dépensée (UTXO). Il est constitué de deux éléments :
* `txid` : l'identifiant de la transaction qui a créé l'output ;
* `vout` : l'index de l'output dans la transaction.

La combinaison de ces deux éléments permet d'identifier précisément un UTXO. Par exemple, si une transaction a un `txid` de `abc...123` et que l'index de l'output est `0`, l'outpoint sera noté :

```text
abc...123:0
```

L'outpoint est utilisé dans les inputs (`vin`) d'une nouvelle transaction pour indiquer quel UTXO est dépensé.

> ► *Le terme « outpoint » est souvent utilisé comme synonyme de « UTXO ».*

