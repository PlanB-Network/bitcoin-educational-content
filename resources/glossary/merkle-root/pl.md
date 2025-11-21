---
term: Merkle Root
---

Digest lub "top Hash" Merkle Tree, który reprezentuje podsumowanie wszystkich informacji obecnych w drzewie. Merkle Tree to struktura akumulatora kryptograficznego, czasami nazywana również "drzewem Hash". W kontekście Bitcoin drzewa Merkle'a są wykorzystywane do organizowania transakcji w ramach bloku i ułatwiania szybkiej weryfikacji włączenia określonej transakcji. Tak więc, w blokach Bitcoin, Merkle Root uzyskuje się poprzez sukcesywne haszowanie transakcji parami, aż pozostanie tylko jeden Hash (Merkle Root). Jest on następnie umieszczany w nagłówku odpowiedniego bloku. To drzewo Hash znajduje się również w UTREEXO, strukturze umożliwiającej kondensację zestawu węzłów UTXO, oraz w MAST Taproot.