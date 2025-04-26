---
term: MERKLE ROOT

---
Digest nebo "top hash" Merklova stromu, který představuje souhrn všech informací obsažených ve stromu. Merkleho strom je kryptografická akumulátorová struktura, někdy také nazývaná "hashovací strom". V kontextu Bitcoinu se Merkleho stromy používají k uspořádání transakcí v rámci bloku a k usnadnění rychlého ověření zařazení konkrétní transakce. V blocích Bitcoinu se tedy Merkleho kořen získává postupným hashováním transakcí po dvojicích, dokud nezůstane pouze jeden hash (Merkleho kořen). Ten je pak zahrnut do záhlaví příslušného bloku. Tento hashovací strom se nachází také v UTREEXO, struktuře, která umožňuje kondenzovat množinu uzlů UTXO, a v MAST Taproot.