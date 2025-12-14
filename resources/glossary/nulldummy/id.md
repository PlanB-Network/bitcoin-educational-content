---
term: NULLDUMMY

---
Aturan konsensus yang diperkenalkan dengan BIP147 di _soft fork_ SegWit yang mengharuskan elemen _dummy_ yang digunakan dalam opcode `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` berupa array _byte_ kosong (`OP_0`). Tindakan ini diimplementasikan untuk menghilangkan vektor maleabilitas dengan melarang nilai apa pun selain `OP_0` untuk elemen ini.
