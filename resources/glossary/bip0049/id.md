---
term: BIP0049

---
BIP49 adalah BIP informatif yang memperkenalkan metode derivasi yang digunakan untuk menghasilkan alamat _Nested_ SegWit di dompet HD. Jalur derivasi yang diusulkan mengikuti standar BIP43 dan BIP44, dengan indeks `49'` (_hardened derivation_) pada kedalaman "tujuan". Sebagai contoh, alamat pertama dari akun P2SH-P2WPKH akan diderivasi melalui jalur: `m/49'/0'/0'/0/0`. Skrip _Nested_ SegWit diciptakan pada saat peluncuran SegWit untuk memfasilitasi adopsinya. Skrip ini memungkinkan penggunaan standar baru ini, bahkan pada dompet yang belum kompatibel dengan SegWit.
