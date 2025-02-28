---
term: PERANGKAT

---
Sebuah protokol yang memungkinkan integrasi data gambar yang diformat secara langsung ke dalam blockchain Bitcoin melalui transaksi multisignature mentah (P2MS). Stamps mengkodekan konten biner dari sebuah gambar dalam basis 64 dan menambahkannya ke kunci 1/3 P2MS. Satu kunci adalah nyata dan digunakan untuk membelanjakan dana, sementara dua lainnya adalah kunci tiruan (kunci pribadi yang terkait tidak diketahui) yang menyimpan data. Dengan mengkodekan data secara langsung sebagai kunci publik daripada menggunakan output `OP_RETURN`, gambar yang disimpan dengan protokol Stamps sangat intensif untuk node. Metode ini secara khusus menciptakan beberapa UTXO, yang meningkatkan ukuran set UTXO dan menimbulkan masalah bagi node yang penuh.