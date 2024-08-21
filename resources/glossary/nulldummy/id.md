---
term: NULLDUMMY
---

Aturan konsensus yang diperkenalkan dengan BIP147 dalam soft fork SegWit yang mengharuskan elemen dummy yang digunakan dalam opcode `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` harus berupa array byte kosong (`OP_0`). Langkah ini diimplementasikan untuk menghilangkan vektor malleability dengan melarang nilai selain `OP_0` untuk elemen ini.