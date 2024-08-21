---
term: JEJAK DOMPET
---

Sebuah set karakteristik khas yang dapat diamati dalam transaksi yang dilakukan oleh dompet Bitcoin yang sama. Karakteristik ini dapat mencakup kesamaan dalam penggunaan tipe skrip, penggunaan kembali alamat, urutan UTXO, penempatan output perubahan, penandaan RBF (*Replace-by-Fee*), nomor versi, bidang `nSequence`, dan bidang `nLockTime`.

Jejak dompet digunakan oleh analis untuk melacak aktivitas entitas tertentu di blockchain dengan mengidentifikasi pola berulang dalam transaksinya. Sebagai contoh, pengguna yang secara sistematis mengirim perubahan mereka ke alamat P2TR (`bc1p…`) menciptakan jejak khas yang dapat digunakan untuk melacak transaksi masa depan mereka.

Seperti yang dijelaskan oleh LaurentMT dalam Space Kek #19 (podcast berbahasa Prancis), kegunaan jejak dompet dalam analisis rantai secara signifikan meningkat seiring berjalannya waktu. Memang, jumlah tipe skrip yang bertambah dan penerapan fitur baru secara bertahap oleh perangkat lunak dompet menonjolkan perbedaan. Bahkan, memungkinkan untuk mengidentifikasi secara akurat perangkat lunak yang digunakan oleh entitas yang dilacak. Oleh karena itu, penting untuk memahami bahwa mempelajari jejak dompet sangat relevan untuk transaksi terkini, lebih dari pada transaksi yang dimulai pada awal tahun 2010-an.