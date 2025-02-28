---
term: TXID (PENGIDENTIFIKASI TRANSAKSI)

---
Pengenal unik yang terkait dengan setiap transaksi Bitcoin. Ini dihasilkan dengan menghitung hash `SHA256d` dari data transaksi. TXID berfungsi sebagai referensi untuk menemukan transaksi tertentu di dalam blockchain. TXID juga digunakan untuk merujuk pada UTXO, yang pada dasarnya merupakan gabungan dari TXID transaksi sebelumnya dan indeks output yang ditunjuk (juga disebut "vout"). Untuk transaksi pasca-SegWit, TXID tidak lagi memperhitungkan saksi transaksi, yang menghilangkan kelenturan.