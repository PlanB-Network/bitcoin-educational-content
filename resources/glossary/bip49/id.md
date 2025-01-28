---
term: BIP49

---
BIP49 adalah BIP informatif yang memperkenalkan metode derivasi yang digunakan untuk menghasilkan alamat SegWit bersarang di dompet HD. Jalur derivasi yang diusulkan mengikuti standar BIP43 dan BIP44, dengan indeks `49'` (derivasi yang diperkeras) pada kedalaman tujuan. Sebagai contoh, alamat pertama dari akun P2SH-P2WPKH akan diturunkan dari jalur: `m/49'/0'/0'/0/0`. Skrip SegWit bersarang diciptakan pada saat peluncuran SegWit untuk memfasilitasi pengadopsiannya. Skrip ini memungkinkan penggunaan standar baru ini, bahkan pada dompet yang belum kompatibel dengan SegWit.