---
term: MERKLE ROOT

---
Merkle'i puu kokkuvõte ehk "top hash", mis kujutab endast kokkuvõtet kogu puus olevast teabest. Merkle'i puu on krüptograafiline akumulaatorstruktuur, mida mõnikord nimetatakse ka "hash-puuks". Bitcoini kontekstis kasutatakse Merkle'i puid tehingute organiseerimiseks plokis ja konkreetse tehingu sisalduse kiire kontrolli hõlbustamiseks. Seega saadakse Bitcoini plokkides Merkle'i juurest järjestikku paarikaupa tehinguid, kuni järele jääb ainult üks hash (Merkle'i juur). Seejärel lisatakse see vastava ploki päisesse. See hash-puu leidub ka UTREEXO struktuuris, mis võimaldab koondada UTXO sõlmede kogumit, ja MAST Taproot'is.