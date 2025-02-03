---
term: NULLDUMMY

---
Aturan konsensus yang diperkenalkan dengan BIP147 di soft fork SegWit yang mengharuskan elemen dummy yang digunakan dalam opcode `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` menjadi array byte kosong (`OP_0`). Tindakan ini diimplementasikan untuk menghilangkan vektor kelenturan dengan melarang nilai apa pun selain `OP_0` untuk elemen ini.