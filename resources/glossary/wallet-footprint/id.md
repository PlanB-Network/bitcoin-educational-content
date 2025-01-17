---
term: JEJAK DOMPET

---
Sekumpulan karakteristik khas yang dapat diamati dalam transaksi yang dilakukan oleh dompet Bitcoin yang sama. Karakteristik ini dapat mencakup kesamaan dalam penggunaan jenis skrip, penggunaan ulang alamat, urutan UTXO, penempatan output perubahan, sinyal RBF (*Replace-by-Fee*), nomor versi, bidang `nSequence`, dan bidang `nLockTime`.

Jejak dompet digunakan oleh para analis untuk melacak aktivitas entitas tertentu pada blockchain dengan mengidentifikasi pola berulang dalam transaksinya. Sebagai contoh, seorang pengguna yang secara sistematis mengirimkan perubahan mereka ke alamat P2TR (`bc1p...`) menciptakan sebuah jejak yang berbeda yang dapat digunakan untuk melacak transaksi mereka di masa depan.

Seperti yang dijelaskan oleh LaurentMT dalam Space Kek #19 (podcast berbahasa Perancis), kegunaan jejak wallet dalam analisis chain meningkat secara signifikan dari waktu ke waktu. Memang, semakin banyaknya jenis skrip dan penyebaran fitur-fitur baru yang semakin bertahap oleh perangkat lunak dompet menonjolkan perbedaannya. Bahkan memungkinkan untuk mengidentifikasi perangkat lunak yang digunakan oleh entitas yang dilacak secara akurat. Oleh karena itu, penting untuk memahami bahwa mempelajari jejak dompet sangat relevan untuk transaksi-transaksi yang baru saja terjadi, lebih dari transaksi yang dimulai pada awal tahun 2010.