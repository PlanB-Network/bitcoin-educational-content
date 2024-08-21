---
term: MERKLE TREE
---

Merkleův strom je kryptografický akumulátor. Jedná se o metodu prokázání členství daného kusu informace v rámci větší sady. Je to datová struktura, která usnadňuje ověřování informací v kompaktním formátu. V systému Bitcoin se Merklovy stromy používají k seskupení a kondenzaci transakcí bloku do jednoho hashe, nazývaného Merklova kořen (nebo "*Root Hash*"). Každá transakce je zahashována, poté jsou sousední hashe hierarchicky zahashovány dohromady, dokud není získán Merklova kořen.

![](../../dictionnaire/assets/1.png)

Tato struktura umožňuje rychlé ověření, zda je konkrétní transakce zahrnuta v daném bloku, aniž by bylo nutné analyzovat všechny transakce. Například, pokud mám pouze Merklova kořen a chci ověřit, že `TX 7` je skutečně součástí stromu, potřeboval bych pouze následující důkazy:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
S těmito informacemi jsem schopen vypočítat mezilehlé uzly až k Merklova kořenu.

![](../../dictionnaire/assets/2.png)

Merklovy stromy se významně používají pro lehké uzly (známé jako "SPV"), které uchovávají pouze hlavičky bloků, ale ne transakce. Tato struktura se také nachází v protokolu UTREEXO, protokolu, který umožňuje kondenzaci sady UTXO uzlů, a v MAST Taproot.

> ► *Merklovy strom je pojmenován po Ralphu Merklovi, kryptografovi, který tuto strukturu navrhl v roce 1979. Merklovy strom lze také nazvat "hash strom". Ve francouzštině se označuje jako "Arbre de Merkle" nebo "arbre de hachage".*