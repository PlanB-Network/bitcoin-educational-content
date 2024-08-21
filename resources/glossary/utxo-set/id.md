---
term: UTXO SET
---

Merujuk pada kumpulan semua UTXO yang ada pada setiap saat tertentu. Dengan kata lain, ini adalah daftar besar dari semua potongan bitcoin yang menunggu untuk dihabiskan. Jika Anda menjumlahkan jumlah dari semua UTXO dalam UTXO set, itu memberi kita total massa moneter dari bitcoin yang beredar. Setiap node dalam jaringan Bitcoin memelihara UTXO setnya sendiri secara real-time. Ini diperbarui saat blok valid baru dikonfirmasi, dengan transaksi yang mereka sertakan, yang mengkonsumsi beberapa UTXO dari UTXO set, dan menciptakan yang baru sebagai gantinya.

UTXO set ini dipertahankan oleh setiap node untuk dengan cepat memverifikasi apakah UTXO yang dihabiskan dalam transaksi memang sah. Ini memungkinkan mereka untuk mendeteksi dan menolak upaya double-spending. UTXO set sering kali menjadi pusat perhatian tentang desentralisasi Bitcoin, karena ukurannya yang secara alami meningkat sangat cepat. Karena sebagian darinya harus disimpan di RAM untuk memverifikasi transaksi dalam waktu yang wajar, UTXO set secara bertahap dapat membuat operasi node penuh menjadi terlalu mahal. UTXO set juga memiliki dampak signifikan pada IBD (*Initial Block Download*). Semakin banyak UTXO set yang dapat ditempatkan di RAM, semakin cepat IBD berlangsung. Pada Bitcoin Core, UTXO set disimpan dalam folder yang bernama `/chainstate`.

> ► *Dalam bahasa Inggris, "UTXO set" dapat diterjemahkan sebagai "UTXO set".*