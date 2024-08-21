---
term: MERKLE ROOT
---

Digest nebo "vrcholový hash" Merkleova stromu, který představuje souhrn všech informací přítomných ve stromu. Merkleův strom je kryptografická akumulační struktura, někdy také nazývaná "hashovací strom". V kontextu Bitcoinu jsou Merkleovy stromy používány k organizaci transakcí v bloku a k usnadnění rychlého ověření začlenění konkrétní transakce. Takže v blocích Bitcoinu je Merkleův kořen získán postupným hashováním transakcí v párech, dokud nezůstane pouze jeden hash (Merkleův kořen). Tento je pak zahrnut v hlavičce příslušného bloku. Tento hashovací strom je také nalezen v UTREEXO, struktuře, která umožňuje kondenzovat UTXO set uzlů, a v MAST Taproot.