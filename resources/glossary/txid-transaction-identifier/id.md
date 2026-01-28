---
term: Txid (identitas transaksi)

definition: Pengidentifikasi unik dari transaksi Bitcoin yang dihitung dengan hash SHA256d dari datanya.
---
Pengenal unik yang terkait dengan setiap transaksi Bitcoin. Ini dihasilkan dengan menghitung hash `SHA256d` dari data transaksi. TXID berfungsi sebagai referensi untuk menemukan transaksi tertentu di dalam _blockchain_. TXID juga digunakan untuk merujuk pada UTXO, yang pada dasarnya merupakan gabungan dari TXID transaksi sebelumnya dan indeks output yang ditunjuk (juga disebut "_vout_"). Untuk transaksi pasca-SegWit, TXID tidak lagi memperhitungkan saksi transaksi, yang menghilangkan maleabilitas.
