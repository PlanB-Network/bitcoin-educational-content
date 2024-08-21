---
term: STAMPS
---

Sebuah protokol yang memungkinkan integrasi data gambar yang diformat langsung ke dalam blockchain Bitcoin melalui transaksi multisignature mentah (P2MS). Stamps mengkodekan konten biner dari sebuah gambar dalam base 64 dan menambahkannya ke kunci-kunci dari 1/3 P2MS. Satu kunci adalah nyata dan digunakan untuk menghabiskan dana, sementara dua kunci lainnya adalah kunci palsu (kunci privat yang terkait tidak diketahui) yang menyimpan data. Dengan mengkodekan data langsung sebagai kunci publik daripada menggunakan output `OP_RETURN`, gambar yang disimpan dengan protokol Stamps secara khusus memerlukan beban kerja yang intensif bagi node-node. Metode ini secara khusus menciptakan banyak UTXO, yang meningkatkan ukuran set UTXO dan menimbulkan masalah bagi node penuh.