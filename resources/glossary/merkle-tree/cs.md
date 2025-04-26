---
term: MERKLE TREE

---
Merklův strom je kryptografický akumulátor. Je to metoda pro dokazování příslušnosti dané informace k větší množině. Je to datová struktura, která usnadňuje ověřování informací v kompaktním formátu. V systému Bitcoin se Merkleho stromy používají k seskupení a zhuštění transakcí bloku do jediného hashe, který se nazývá Merkleho kořen (nebo "*Kořenový hash*"). Každá transakce se hashuje, pak se sousední hashe hierarchicky hashují dohromady, dokud se nezíská Merkleho kořen.

![](../../dictionnaire/assets/1.webp)

Tato struktura umožňuje rychle ověřit, zda je konkrétní transakce zahrnuta v daném bloku, aniž by bylo nutné analyzovat všechny transakce. Například pokud mám k dispozici pouze Merkleho kořen a chci ověřit, že `TX 7` je skutečně součástí stromu, stačí mi následující důkazy:


- `TX 7`;
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

S těmito informacemi jsem schopen vypočítat mezilehlé uzly až po Merkleho kořen.

![](../../dictionnaire/assets/2.webp)

Merkleho stromy se používají zejména pro lehké uzly (známé jako "SPV"), které uchovávají pouze hlavičky bloků, ale ne transakce. Tato struktura se vyskytuje také v protokolu UTREEXO, protokolu, který umožňuje kondenzaci sady uzlů UTXO, a v protokolu MAST Taproot.

> ► *Merkleho strom je pojmenován po Ralphu Merklem, kryptografovi, který tuto strukturu v roce 1979 navrhl. Merkleho strom se může nazývat také "hashovací strom". Ve francouzštině se označuje jako "Arbre de Merkle" nebo "arbre de hachage".*