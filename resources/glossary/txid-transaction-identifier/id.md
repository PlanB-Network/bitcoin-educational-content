---
term: TXID (TRANSACTION IDENTIFIER)
---

Sebuah pengenal unik yang terkait dengan setiap transaksi Bitcoin. TXID dihasilkan dengan menghitung hash `SHA256d` dari data transaksi. TXID berfungsi sebagai referensi untuk menemukan transaksi spesifik dalam blockchain. TXID juga digunakan untuk merujuk pada UTXO, yang pada dasarnya adalah penggabungan dari TXID transaksi sebelumnya dan indeks output yang ditunjuk (juga disebut "vout"). Untuk transaksi pasca-SegWit, TXID tidak lagi memperhitungkan saksi transaksi, yang menghilangkan kemungkinan perubahan.