---
term: SET UTXO

---
Mengacu pada koleksi semua UTXO yang ada pada saat tertentu. Dengan kata lain, ini adalah daftar besar dari semua bagian bitcoin yang berbeda yang menunggu untuk dibelanjakan. Jika Anda menjumlahkan jumlah semua UTXO dalam kumpulan UTXO, maka akan menghasilkan jumlah total uang bitcoin yang beredar. Setiap node dalam jaringan Bitcoin menyimpan set UTXO-nya sendiri secara real-time. Ia memperbaruinya ketika blok baru yang valid dikonfirmasi, dengan transaksi yang disertakan, yang mengkonsumsi beberapa UTXO dari set UTXO, dan membuat yang baru sebagai gantinya.

Kumpulan UTXO ini disimpan oleh setiap node untuk memverifikasi dengan cepat apakah UTXO yang dibelanjakan dalam transaksi memang sah. Hal ini memungkinkan mereka untuk mendeteksi dan menolak upaya pembelanjaan ganda. Kumpulan UTXO sering kali menjadi pusat perhatian mengenai desentralisasi Bitcoin, karena ukurannya yang secara alami meningkat dengan sangat cepat. Karena sebagian harus disimpan dalam RAM untuk memverifikasi transaksi dalam waktu yang wajar, set UTXO secara bertahap dapat membuat pengoperasian sebuah node penuh menjadi terlalu mahal. Set UTXO juga memiliki dampak yang signifikan terhadap IBD (*Initial Block Download*). Semakin banyak set UTXO yang dapat ditempatkan di RAM, semakin cepat IBD-nya. Pada Bitcoin Core, set UTXO disimpan dalam folder bernama `/chainstate`.

> ► *Dalam bahasa Inggris, "UTXO set" dapat diterjemahkan sebagai "set UTXO".*