---
term: PEMBAYARAN BERKALA

---
Sebuah heuristik internal untuk analisis rantai Bitcoin yang memungkinkan sebuah hipotesis mengenai sifat output dari sebuah transaksi berdasarkan jumlah bulat. Umumnya, ketika dihadapkan pada pola pembayaran sederhana (1 input dan 2 output), jika salah satu output mengeluarkan jumlah yang bulat, maka output tersebut merepresentasikan pembayaran. Dengan eliminasi, jika satu output mewakili pembayaran, maka output lainnya mewakili kembalian. Oleh karena itu, dapat diartikan bahwa kemungkinan pengguna yang memasukkan transaksi masih memiliki output yang diidentifikasi sebagai kembalian.

Perlu dicatat bahwa heuristik ini tidak selalu dapat diterapkan, karena sebagian besar pembayaran masih dilakukan dalam satuan mata uang fiat. Memang, ketika seorang pedagang di Perancis menerima bitcoin, umumnya, mereka tidak menampilkan harga yang stabil dalam sat. Mereka lebih suka memilih konversi antara harga dalam euro dan jumlah bitcoin yang akan dibayarkan melalui POS mereka (seperti BTCPay Server, misalnya). Oleh karena itu, seharusnya tidak ada angka bulat dalam output transaksi. Namun demikian, seorang analis dapat mencoba melakukan konversi ini dengan memperhitungkan nilai tukar yang berlaku saat transaksi disiarkan di jaringan. Jika suatu hari nanti, bitcoin menjadi unit akun yang lebih disukai di bursa kami, heuristik ini dapat menjadi lebih berguna untuk analisis.

![](../../dictionnaire/assets/11.webp)